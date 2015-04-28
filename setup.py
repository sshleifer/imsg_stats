"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['imsg_stats.py']
DATA_FILES = ['contacts.py', 'chat_to_csv.py']
OPTIONS = {'argv_emulation': True, "resources":["index.html"]}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)