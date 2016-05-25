#!/usr/bin/env python3
"""Setting.

This file contains the logic of settings screens.
"""


from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from section import Section
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
        # if self.active is True and self.ids.pr1.text
        # is not self.ids.pr2.text:
        # print(self.ids.pr1.focus)
        # popup = InfoPopup()
        # popup.set_info('Root passwords do not match')
        # popup.open()
        user = User()
        user.save_user(root_pass, username, user_pass, home, shell)
        section = Section()
        section.create_file()
