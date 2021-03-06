#!/usr/bin/env python3
"""Setting.

This file contains the logic of settings screens.
"""


from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from locale import Locale
from section import Section
from script import Script
from source import Source
from user import User


Builder.load_file('settings.kv')


class InfoPopup(Popup):
    """Popup."""

    info = StringProperty('')

    def set_info(self, message):
        """Write a message into Popup window."""
        self.info = message

    def on_press_dismiss(self, *args):
        """On press."""
        self.dismiss()
        return False


class Settings(Screen):
    """Settings screen."""

    # Properties interacting with the user settings form.
    root_pass_state = root_pass_conf_state = BooleanProperty(True)
    source = ''
    locale = Locale()
    languages = ListProperty()
    # languages = locale.get_locale()
    keyboards = locale.get_keyboard()
    timezones = locale.get_timezone()

    def search(self, text):
        """Search function."""
        if text and not text.strip():
            self.languages = list(set(self.locale.get_locale()))
            self.languages.sort()
        elif text == '':
            self.languages = list(set(self.locale.get_locale()))
            self.languages.sort()
        else:
            self.languages = self.locale.search_language(text)

    def callback(self, instance):        
        print("HI" + str(instance))

    def active_root(self, instance, value):
        """Print."""
        self.active = value
        if self.active is True:
            self.root_pass_state = False
            self.ids.pr1.focus = True
        elif self.active is False:
            self.root_pass_conf_state = True
            self.ids.pr1.text = ''
            self.ids.pr2.text = ''

    def group_source(self, instance, text):
        """Group button."""
        self.source = text

    def check_root_pass(self, instance, value):
        """Check root password."""
        if not value:
            if self.ids.pr1.text != self.ids.pr2.text:
                popup = InfoPopup()
                popup.set_info('Root passwords do not match')
                popup.open()

    def validate_forms(self):
        """Validate form."""
        root_pass = self.ids.pr2.text
        username = self.ids.us1.text
        user_pass = self.ids.us3.text
        home = self.ids.us4.text
        shell = self.ids.us5.text

        pre = self.ids.pre.text
        pos = self.ids.pos.text

        if self.source:
            s = self.source
        else:
            s = 'cdrom'

        folder = ''
        server = ''
        partition = self.ids.partition.text
        ftp_user = self.ids.ftp_user.text
        ftp_pass = self.ids.ftp_pass.text

        print('SOURCE:' + self.source)
        if s == 'Hard drive':
            folder = self.ids.hh_folder.text
        elif s == 'NFS':
            folder = self.ids.nfs_folder.text
            server = self.ids.nfs_server.text
        elif s == 'HTTP':
            folder = self.ids.http_folder.text
            server = self.ids.http_server.text
        elif s == 'FTP':
            folder = self.ids.ftp_folder.text
            server = self.ids.ftp_server.text

        source = Source()
        source.save_source(s, partition, folder, server, ftp_user, ftp_pass)

        # if self.active is True and self.ids.pr1.text
        # is not self.ids.pr2.text:
        # print(self.ids.pr1.focus)
        # popup = InfoPopup()
        # popup.set_info('Root passwords do not match')
        # popup.open()
        user = User()
        user.save_user(root_pass, username, user_pass, home, shell)
        script = Script()
        script.save_script(pre, pos)
        section = Section()
        section.create_file()
