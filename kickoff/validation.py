#!/usr/bin/env python3
"""Kickstart file validator.

Check syntax of the file kick start file.
"""


from os import system


class Validate:
    """Class in order to validate Kickstart file."""

    @classmethod
    def ksvalidate(cls, kstext):
        """Construtor class, create a tmp file and check."""
        ksfile = open('/tmp/ks.cfg', 'w+')
        if kstext:
            ksfile.write(kstext)
            ksfile.close()
            # I am using the ksvalidator, I tried to use the pykickstart
            # modules directly but I couldn't do because, the python 3 version
            # produce an error, I will try again in another time.
            check = system("ksvalidator /tmp/ks.cfg")
            if int(check) == 0:
                return 'PASS'
            else:
                return 'FAIL'
        else:
            return 'FAIL'
