#!/usr/bin/env python3
"""Section class.

This file has the secion class.
"""


class Section:
    """Build the kickstart file."""

    ks = []

    comment = {'user': '# Creates a new user on the system'}

    ksfile = {}

    def save_section(self, name, section):
        """Save every section."""
        section = self.comment[name] + '\n' + section[0]
        ksfile = {name: section}
        print(ksfile)
