#!/usr/bin/env python3
"""Source installation class.

This class manage the diferent parts of the source installation.
"""

from section import Section


class Source(Section):
    """Manage the diferents  installation method CD-ROM, Hard drive, NFS ..."""

    def save_source(self, s, partition, folder, server, ftp_user, ftp_pass):
        """Save and format the source in the kickstart file."""
        self.ks = []

        if s == 'cdrom':
            self.ks.append('cdrom')
        elif s == 'Hard drive':
            self.ks.append('harddrive --partition=' + partition +
                           ' --dir=' + folder)
        elif s == 'NFS':
            self.ks.append('nfs --server=' + server + ' --dir=' + folder)
        elif s == 'HTTP':
            self.ks.append('url --url ' + server + '/' + folder)
        elif s == 'FTP':
            self.ks.append('url --url ftp://' + ftp_user + ':' + ftp_pass +
                           '@' + server + '/' + folder)
        else:
            self.ks.append('cdrom')

        self.save_section('source', self.ks)
