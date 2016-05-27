#!/usr/bin/env python3
"""Section class.

This file has the secion class.
"""


class Section:
    """Build the kickstart file."""

    ks = []

    # Dictionary of comments for each section.
    comment = {'user': '# Creates a new user on the system',
               'root': '# Sets the system\'s root password',
               'pre': '# Pre-installation Script',
               'post': '# Pos-installation Script'}

    ksfile = {}

    kstext = ""

    def save_section(self, name, section):
        """Save every section."""
        section = self.comment[name] + '\n' + section[0] + '\n'
        self.ksfile[name] = section
        print(self.ksfile)

    def create_file(self):
        """Create ks file."""
        # Creating the file if doesn't exits.
        kickstart = open('/tmp/ks.cfg', 'w+')
        kickstart.close()
        # Append lines to the file.
        kickstart = open('/tmp/ks.cfg', 'a')
        for k, v in self.ksfile.items():
            kickstart.write(v)
        kickstart.close()

    def load_files(self):
        """Changing file."""
        self.create_file()
        kickstart = open('/tmp/ks.cfg', 'r')
        self.kstext = ""
        tmp = kickstart.read()
        for line in tmp:
            self.kstext += line
        return self.kstext
