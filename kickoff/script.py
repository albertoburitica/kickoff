#!/usr/bin/env python3
"""Scripts.

This file contiains the scripts class and methods in this receive the pre and
pos scripts in order to add to the kickstart file.
"""


from section import Section


class Script(Section):
    """Script class."""

    def save_script(self, pre, pos):
        """Saving the pre and pos scripts into the dictionary."""
        self.ks = []
        if pre:
            self.prepare_script('pre', pre)
        elif not pre and self.ksfile.get('pre') is not None:
            del self.ksfile['pre']

        if pos:
            self.prepare_script('post', pos)
        elif not pos and self.ksfile.get('post') is not None:
            del self.ksfile['post']

    def prepare_script(self, t, script):
        """Formatting the script to save in the ks list."""
        self.ks.append('%' + t + '\n' + script + '\n' + '%end')
        self.save_section(t, self.ks)
        print(self.ks)
        self.ks = []
