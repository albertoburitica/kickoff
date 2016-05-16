#!/usr/bin/env python3
"""Kickstart file validator.

Check syntax of the file kick start file.
"""


from os import system


class Validate:
    """Class in order to validate Kickstart file."""

    @classmethod
    def ksvalidate(self, kstext):
        """Construtor class, create a tmp file and check."""
        ksfile = open('/tmp/ks.cfg', 'w+')
        ksfile.write(kstext)
        ksfile.close()
        check = system("ksvalidator /tmp/ks.cfg")
        if int(check) == 0:
            return "PASS"
        else:
            return "FAIL"
