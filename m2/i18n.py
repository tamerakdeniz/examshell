"""Shared UI language, loaded from the user's profile."""
import json
from pathlib import Path

_language = 'en'
ENGLISH = json.loads(Path(__file__).with_name('en.json').read_text())


def set_language(language):
    global _language
    if language not in ('en', 'tr'):
        raise ValueError('Unsupported language')
    _language = language


def language():
    return _language


def t(message, *values):
    template = ENGLISH[message] if _language == 'en' else message
    return template.format(*values) if values else template


def subject_path(directory):
    return directory / ('README.tr.md' if _language == 'tr' else 'README.md')
