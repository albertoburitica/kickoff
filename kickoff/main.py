#!/usr/bin/env python3
"""Main windows GUI kickoff app.

This file contain the code of the main windows.
"""


from validation import Validate
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock


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
        """Validating."""
        self.progress = 0
        Clock.schedule_interval(self.update_progressbar, 1 / 60)

    def update_progressbar(self, dt):
        if self.progress != 100 and self.progress != -1:
            self.progress += 1
            self.status = 'Validating: {}%'.format(int(self.progress))
        elif self.progress == 100:
            check = Validate.ksvalidate(self.kstext)
            self.progress = -1
            self.status = check

class MainWindowApp(App):
    """Class MainWindowApp."""

    def build(self):
        """Build function."""
        self.title = "Kickoff | Kickstart file configurator"
        return MainWindow()

if __name__ == "__main__":
    MainWindowApp().run()