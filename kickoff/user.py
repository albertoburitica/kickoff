#!/usr/bin/env python3
"""Section class.

This file has the secion class.
"""

from section import Section
from subprocess import getoutput


class User(Section):
    """Build user section."""

    def save_user(self, username, user_pass, home, shell):
        """Save user section."""
        self.ks = []
        user_pass = self.encrypt_passwd(user_pass)
        user = 'user --name=' + username + ' --password=' + user_pass +  \
               ' --iscrypted'
        if home:
            user += ' --homedir=homedir'
        if shell:
            user += ' --shell=' + shell
        self.ks.append(user)
        self.save_section('user', self.ks)

    def encrypt_passwd(self, passwd):
        """Encrypt password using openssl."""
        passwd = getoutput('openssl passwd -1 ' + passwd)
        return passwd
