
#!/usr/bin/env python3
"""Setup.py file.

Installation file setup.py of kickoff project.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
           "description": "My Project",
           "author": "Alberto Buritica",
           "url": "URL to get it at",
           "download_url": "Where to download it",
           "author_email": "alberto.buritica@outlook.es",
           "version": "0.1",
           "install_requires": ['nose', 'pykickstart'],
           "packages": ['kickoff'],
           "scripts": [],
           "name": 'kickoff'
         }

setup(**config)
