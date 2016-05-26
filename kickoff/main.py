#!/usr/bin/env python3
"""Main windows GUI kickoff app.

This file contain the code of the main windows.
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from section import Section
from settings import Settings
from validation import Validate


Builder.load_file('main.kv')


class MainWindow(Screen):
    """Class MainWindow."""

    status = StringProperty("")
    progress = NumericProperty(0)
    kstext = StringProperty("")

    section = Section()

    def load_file(self):
        """Loading the kickstart file into textbox."""
        self.kstext = self.section.load_files()

    def close(self):
        """Close function. Function which the button close call."""
        exit(0)

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

# Screen manager.
screen = ScreenManager(transition=WipeTransition())
screen.add_widget(Settings(name='settings'))
screen.add_widget(MainWindow(name='main'))


class MainWindowApp(App):
    """Class MainWindowApp."""

    def build(self):
        """Build the main window and set the title."""
        self.title = "Kickoff | Kickstart file configurator"
        # return MainWindow()
        return screen

if __name__ == "__main__":
    MainWindowApp().run()
