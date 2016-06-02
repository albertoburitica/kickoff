#!/usr/bin/env python3
"""Locale manage.

This file get locale information forn the file locale-list.
"""


from re import compile


class Locale:
    """Locale class."""

    locales = {}
    language = []

    types_keyboard = {}
    lang_keyboard = []

    timezones = []

    def get_locale(self):
        """Get locale language list from locale-list file."""
        patten = compile(r'(\w+_\w{2})')
        locale_list = open('locale-list')
        for line in locale_list:
            code = patten.search(line)
            lang = line[len(code.group()):].replace('\n', '').lstrip()
            self.locales[code.group()] = lang
            self.language.append(lang)
        self.language.sort()
        return self.language

    def search_language(self, text):
        """Searching language."""
        language = self.get_locale()
        tmp = []
        for l in language:
            if l.lower().startswith(text.lower()):
                tmp.append(l)
        tmp = list(set(tmp))
        return tmp

    def get_keyboard(self):
        """Get keyboard list from keyboard-list file."""
        keyboard_list = open('keyboard-list')
        for line in keyboard_list:
            line = line.split('*')
            self.types_keyboard[line[0]] = line[1].replace('\n', '')
            self.lang_keyboard.append(line[1].replace('\n', ''))
        self.lang_keyboard.sort()
        return self.lang_keyboard

    def get_timezone(self):
        """Get the timzones from the file timezone-list file."""
        timezone_list = open('timezone-list')
        for line in timezone_list:
            self.timezones.append(line.replace('\n', ''))
        self.timezones.sort()
        return self.timezones
