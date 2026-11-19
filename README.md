# ExamShell

ExamShell is a practice environment for 42 milestone exams, with a local C grader, a split VS Code workspace and optional Gemini assistance.

Milestone 2 is currently available with 53 questions across four levels. The milestone selector provides the entry point for future M3, M4 and other milestone support.

## Supported milestones

| Milestone | Status | Question bank |
|---|---|---|
| M2 | Available | 53 questions, 4 levels |
| M3, M4 and beyond | Future additions | To be added |

## Install

Requirements: macOS or Linux, Python 3.9+, Git and a C compiler available as `cc` (Clang or GCC). Install VS Code for the editor workflow. Python uses only the standard library.

```sh
git clone https://github.com/tamerakdeniz/examshell.git
cd examshell
python3 examshell.py
```

To run `examshell` from any directory, run these commands inside the cloned repository:

```sh
mkdir -p ~/.local/bin
ln -s "$PWD/examshell.py" ~/.local/bin/examshell
```

If needed, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` or `~/.bashrc`, then open a new terminal. Keep the cloned directory in place so the link continues to work.

## Language and first launch

Choose **English** or **Türkçe** on first launch. Enter selects English. Your preference is saved in your profile and reused on subsequent launches, including when resuming a session. Existing profiles are prompted once after upgrading.

Use `/lang` to reopen the language menu, or `/lang en` and `/lang tr` to switch directly. The terminal, subject and VS Code buttons update immediately. All 53 Turkish subjects are bundled as `subject.tr.txt` language resources for offline use. Repository documentation is maintained in English. Function names, filenames and example inputs/outputs keep their original form.

Select M2 in the milestone menu. You can skip the optional Gemini API key prompt with Enter. Start an exam with `/exam` or configure practice with `/practice`.

## Editor workflow

VS Code opens with your submission on the left and the subject on the right. Write your code and click **Grade** in the status bar. It saves changed files in the active submission directory and runs the local grader. Failed tests appear in the **M2 · Grade** output panel. Passing loads the next question.

**View solution** opens the short or alternative solution. **Compare** opens a diff against your submission. **Subject** restores the split layout. Commands are also available under `M2:` in the command palette.

Keep the ExamShell terminal open during the session. The app loads its bundled extension into a dedicated window, which may be titled “Extension Development Host”. If VS Code asks about workspace trust, approve the generated practice directory. Linux requires `code` on PATH. On macOS the standard VS Code application location is also recognized.

Use `examshell --terminal` for terminal-only practice.

## Modes and progress

- **Exam** progresses through levels 1–4 with one random question per level. Failed submissions stay on the same question. Previously completed questions can appear.
- **Practice** supports one or more levels, ordered rotation or random selection, and including or excluding completed questions.
- With repeats disabled, questions passed in any previous exam or practice session are excluded. Empty levels are skipped and practice ends when the pool is exhausted.
- Where another eligible question exists, selection avoids the last question shown at that level.
- `/quit` saves and exits for later resumption. `exit` ends the session and exits. `/end` ends the session while keeping the shell open. Files and solved-question history are retained.

| Command | Action |
|---|---|
| `/exam`, `/practice` | Start a session |
| `/subject`, `/path` | Show the subject or submission path |
| `/grade`, `grademe` | Compile and test saved code |
| `/answer [long]` | View the short or alternative solution |
| `/diff [long]` | Compare your code with a solution |
| `/progress` | Show solved counts per level |
| `/lang [en\|tr]` | Change language |
| `/update` | Check and install updates |
| `/api-key`, `/model` | Configure Gemini |
| `/ai <question>` | Ask about your code and last test result |
| `/help` | Show commands |

The milestone menu also accepts `/lang`, `/update` and `/help`.

## Local grading

Program tests compare stdout byte for byte. Function tests compile a separate C driver that calls the public function and prints its result. A failure shows the first failing input, expected output, actual output or compiler error. Each test has a two-second timeout.

Tests implement subject-based behavior checks. Official hidden Moulinette tests, Norm checking, forbidden-function detection and memory-leak checks are outside the grader's coverage. Submissions run under your local user account.

The bank comes from the project owner's M2 practice collection. Short solutions live in `main.c`, alternative solutions in the named C files. Some imported solution defects were corrected, including function names, example-main conflicts and empty-input handling. The `hiddenp` and `sort_in_tab` directories use the subject's submission names `hidenp.c` and `sort_int_tab.c`.

## Gemini and local data

The model selector includes `gemini-3.5-flash-lite`, `gemini-3.8-flash`, `gemini-2.5-flash` and `gemini-3.1-flash-lite`. Availability depends on your account and the provider's model lifecycle.

Only `/ai` sends your active subject, submission C/header files, last test result and question to Gemini. The prompt requests an answer in your selected language.

Settings, progress and submissions live in `~/.m2-examshell/`. Saved API keys are unencrypted in an owner-readable `config.json`. To use an environment variable instead, skip the key prompt and set `GEMINI_API_KEY`. Create a separate profile with `examshell --home ~/.m2-second-profile`.

## Updates

Startup checks `origin/main` and suggests `/update` when new commits exist. Both `update` and `/update` work. Updates require a clean Git clone on `main` and use a fast-forward merge. Local changes or diverged history stop the update with an explanation. Network failures allow normal practice to continue.

After installation the app exits with your session saved. Close the ExamShell VS Code window and run `examshell` again to load the updated Python code and extension.

## Development

```sh
python3 -m unittest discover -s tests -v
node --check vscode/extension.js
```

Tests cover both reference solutions for every question, session lifecycle, update behavior and language persistence/switching. Automated tests use local fixtures rather than Gemini requests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution and README guidelines.
