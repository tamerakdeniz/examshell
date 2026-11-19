# Contributing to ExamShell

ExamShell consists of an exam and practice application built with the Python standard library and a VS Code extension written in JavaScript. M2 is currently supported, with additional milestones planned.

## Development environment

Clone the repository and install Python 3.9+, Clang or GCC, and VS Code. Node.js is used to check JavaScript syntax. Use a separate profile for development.

```sh
python3 examshell.py --terminal --home /tmp/examshell-development
python3 -m unittest discover -s tests -v
node --check vscode/extension.js
```

Omit `--terminal` to test the editor workflow. You can skip the API key prompt when creating a test profile.

## Project layout

| Path | Purpose |
|---|---|
| `examshell.py` | Milestone selection, sessions, practice and commands |
| `m2/grader.py` | C compilation, execution and result comparison |
| `m2/cases.py` | Program test cases and function drivers |
| `m2/editor.py` | File-based communication between Python and VS Code |
| `m2/ai.py` | Gemini client |
| `m2/i18n.py`, `m2/en.json` | Language selection and interface translations |
| `m2/updater.py` | Startup update checks and fast-forward installation |
| `vscode/` | VS Code extension and commands |
| `bank/level*/` | Subjects, language resources, solutions and headers |
| `tests/` | Python regression tests |

## Reporting bugs

Include your operating system, Python version, terminal or editor mode, question name and steps to reproduce the issue. Describe the expected and actual behavior. For grading failures, include the relevant input and output. Keep API keys and personal profile files out of reports.

## Submitting changes

1. Create a branch in your fork.
2. Group commits by meaningful scope, such as the question bank, application behavior, editor integration or documentation.
3. Verify the changed behavior with the existing tests. When fixing a bug, add a regression test that reproduces it.
4. Describe the problem, resulting behavior and verification in your pull request.

For editor changes, check that the submission on the left matches the subject on the right. Verify saving through Grade, staying on the same question after failure, and advancing after success. Check starting a new session after `exit` and resuming the same question after `/quit`.

## Adding questions

Place each question in the appropriate `bank/levelN/question_name/` directory. Use `README.md` for the English subject, `main.c` for the short solution and `question_name.c` for the alternative solution. Put required headers in the same directory. If the submission filename differs from the directory name, update the mapping in `m2/grader.py`.

For program questions, add argument and expected-output pairs. For function questions, add a C driver and expected results. Test both solutions. Update displayed question counts and documentation when the bank changes. Derive expected outputs from the subject.

When adding a milestone, define its question bank, grader and persistence layout. Preserve compatibility with existing M2 progress files.

## Documentation guidelines

Write all repository Markdown documentation in English. Keep the README usable for someone cloning the project for the first time. Update the relevant sections when commands, installation requirements or session behavior change. Clearly identify supported features and behavior that still needs verification.

Preserve function names, filenames and literal sample inputs and outputs in subjects.

## Language support

English is the default application language. Python interface messages use `m2/i18n.py` and `m2/en.json`. Add the English equivalent of a Turkish message key to the catalog and display it through `t()`. VS Code buttons use the session's `language` value.

For new questions, add the Turkish subject as `subject.tr.txt` alongside the English `README.md`. These text files are runtime language resources. Keep filenames, prototypes and example inputs and outputs consistent across languages.

Verify that changing language updates the active subject while preserving the submission, session and progress.
