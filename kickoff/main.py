#!/usr/bin/env python3
"""Main windows GUI kickoff app.

This file contain the code of the main windows.
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.uix.settings import Settings
from kivy.clock import Clock
from validation import Validate


Builder.load_file('main.kv')


class MainWindow(BoxLayout):
    """Class MainWindow."""

    status = StringProperty("")
    progress = NumericProperty(0)
    kstext = """#Do not configure the X Window System
skipx
%pre
mkdir /etc/pre
%end
%post
mkdir /etc/post
%end"""

    def close(self):
        """Close function. Function which the button close call."""
        exit(0)

    def file_content(self):
        """File content function."""
        pass

    def validate(self):
        """Calling the function update_progressbar."""
        self.progress = 0
        Clock.schedule_interval(self.update_progressbar, 1 / 60)

    def update_progressbar(self, dt):
        """Updating progress bar and activating validation."""
        if self.progress != 100 and self.progress != -1:
            self.progress += 1
            self.status = 'Validating: {}%'.format(int(self.progress))
        elif self.progress == 100:
            check = Validate.ksvalidate(self.kstext)
            self.progress = -1
            self.status = check





class MainWindowApp(App):
    """Class MainWindowApp."""

    use_kivy_settings = True    

    def build(self):
        """Build the main window and set the title."""
        self.settings_cls = KickoffSettings
        self.title = "Kickoff | Kickstart file configurator"
        return MainWindow()

    def build_config(self, config):
        """Initial settings."""
        config.setdefaults('User settings', 
                           {
                            'root': 1,
                            'username': 'aburitica'
                           })

    def build_settings(self, settings):
        """Using .json file and load."""
        with open("settings.json") as s_json:
            settings.add_json_panel('User settings', self.config,
                                    data=s_json.read())

class KickoffSettings(Settings):
    pass


if __name__ == "__main__":
    MainWindowApp().run()
