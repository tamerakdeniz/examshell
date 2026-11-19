const vscode = require('vscode');
const fs = require('node:fs/promises');
const path = require('node:path');

exports.activate = async function (context) {
    const root = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (!root) return;
    const output = vscode.window.createOutputChannel('M2 · Grade');
    const items = [];
    const documents = new Map();
    let current, revision, resultRevision, pending = false;
    const file = name => path.join(root, name);
    const read = async name => JSON.parse(await fs.readFile(file(name), 'utf8'));
    const show = (uri, column) => vscode.window.showTextDocument(uri, {viewColumn: column, preview: false});
    context.subscriptions.push(output, vscode.workspace.registerTextDocumentContentProvider('m2-exam', {
        provideTextDocumentContent: uri => documents.get(uri.toString()) || ''
    }));

    function reference(label, content) {
        const uri = vscode.Uri.from({scheme: 'm2-exam', path: '/' + current.ticket + '/' + label});
        documents.set(uri.toString(), content);
        return uri;
    }
    async function display(action, alternative) {
        if (!current || current.action === 'closed') return;
        const submission = vscode.Uri.file(file(current.ticket));
        const answer = () => reference(alternative ? 'Uzun çözüm.c' : 'Kısa çözüm.c',
                                       alternative ? current.long : current.short);
        if (action === 'diff') {
            await vscode.commands.executeCommand('vscode.diff', submission, answer(),
                'Teslim ↔ ' + (alternative ? 'Uzun çözüm' : 'Kısa çözüm'), {viewColumn: vscode.ViewColumn.One});
        } else if (action === 'answer') {
            await show(answer(), vscode.ViewColumn.One);
        } else {
            await vscode.commands.executeCommand('vscode.setEditorLayout', {
                orientation: 0, groups: [{size: 0.55}, {size: 0.45}]
            });
            const subject = current.subject.replace(/^## Subject\s*\n```[^\n]*\n/, '').replace(/\s*```\s*$/, '');
            await show(reference('Subject.txt', subject), vscode.ViewColumn.Two);
            await show(submission, vscode.ViewColumn.One);
        }
    }

    for (const [action, label] of [['grade','$(play) Grade'], ['answer','Cevabı gör'], ['diff','Karşılaştır'], ['subject','Subject']]) {
        const command = 'm2.' + action;
        const item = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 110 - items.length);
        item.text = label;
        item.command = command;
        items.push(item);
        context.subscriptions.push(item, vscode.commands.registerCommand(command, async () => {
            try {
                if (!current || current.action === 'closed') return;
                if (action === 'grade') {
                    if (pending) return;
                    const {ticket, attempt} = current;
                    const shown = vscode.window.activeTextEditor?.document.uri;
                    if (shown?.scheme === 'file' && path.dirname(shown.fsPath) !== path.dirname(file(ticket))) {
                        await display('subject');
                        vscode.window.showInformationMessage('Güncel teslim açıldı. Kontrol ettikten sonra Grade düğmesine bas.');
                        return;
                    }
                    pending = true;
                    try {
                        const folder = path.dirname(file(ticket));
                        for (const doc of vscode.workspace.textDocuments) {
                            if (doc.isDirty && doc.uri.scheme === 'file' && path.dirname(doc.uri.fsPath) === folder) {
                                if (!await doc.save()) throw Error('Teslim dosyası kaydedilemedi.');
                            }
                        }
                        const tmp = file('.m2-grade.tmp');
                        await fs.writeFile(tmp, JSON.stringify({ticket, attempt}));
                        await fs.rename(tmp, file('.m2-grade.json'));
                        item.text = '$(sync~spin) Grade';
                    } catch (e) { pending = false; throw e; }
                } else if (action === 'subject') {
                    await display(action);
                } else {
                    const choice = await vscode.window.showQuickPick(['Kısa çözüm','Uzun çözüm']);
                    if (choice) await display(action, choice === 'Uzun çözüm');
                }
            } catch (e) { vscode.window.showErrorMessage(String(e.message)); }
        }));
    }

    async function refresh() {
        try {
            const result = await read('.m2-result.json');
            if (result.revision !== resultRevision) {
                resultRevision = result.revision;
                pending = false;
                items[0].text = '$(play) Grade';
                output.appendLine(result.ticket + '\n' + result.message);
                if (result.ok) vscode.window.showInformationMessage(result.message);
                else output.show(true);
            }
        } catch (e) { if (e.code !== 'ENOENT') throw e; }
        const next = await read('.m2-view.json');
        if (next.revision === revision) return;
        if (next.attempt !== current?.attempt || next.action === 'closed') {
            pending = false;
            items[0].text = '$(play) Grade';
            const stale = vscode.window.tabGroups.all.flatMap(group => group.tabs).filter(tab => {
                if (tab.isDirty) return false;
                const uri = tab.input?.uri || tab.input?.original;
                if (!uri) return false;
                if (uri.scheme === 'm2-exam') return true;
                const rel = path.relative(root, uri.fsPath);
                return uri.scheme === 'file' && /^[a-f0-9]{32}\/\d+\//.test(rel)
                    && (next.action === 'closed' || path.dirname(rel) !== path.dirname(next.ticket));
            });
            if (stale.length) await vscode.window.tabGroups.close(stale, true);
        }
        current = next;
        if (current.action === 'closed') {
            items.forEach(item => item.hide());
        } else {
            items.forEach(item => item.show());
            await display(current.action, current.alternative);
            await fs.writeFile(file('.m2-ready'), current.revision);
        }
        revision = current.revision;
    }
    let queue = Promise.resolve();
    const update = () => {
        queue = queue.then(refresh).catch(e => vscode.window.showErrorMessage('M2: ' + e.message));
    };
    const watcher = vscode.workspace.createFileSystemWatcher(new vscode.RelativePattern(root, '.m2-{view,result}.json'));
    context.subscriptions.push(watcher, watcher.onDidChange(update), watcher.onDidCreate(update));
    const timer = setInterval(update, 800);
    context.subscriptions.push({dispose: () => clearInterval(timer)});
    update();
};
