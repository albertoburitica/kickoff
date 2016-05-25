#!/usr/bin/env python3
"""Section class.

This file has the secion class.
"""

from section import Section
from subprocess import getoutput


class User(Section):
    """Build user section."""

    def save_user(self, root_pass, username, user_pass, home, shell):
        """Save user section."""
        self.ks = []

        # Encrypting the password.
        if root_pass:
            root_pass = self.encrypt_passwd(root_pass)
            root = 'rootpw --iscrypted ' + root_pass
            self.ks.append(root)
            self.save_section('root', self.ks)
            self.ks = []
        else:
            self.ks = []

        # Encrypting the password.
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
