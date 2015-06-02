"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['imsg_stats.py']
DATA_FILES = ['index.html',
              'scatter2.js',
              'steamgraph.html',
              'steamgraph.js',
              'cs2.html',
              'cs2.js',
              'js_sources/dc.min.js',
              'js_sources/dc.min.js.map',
              'js_sources/crossfilter.min.js',
              'js_sources/bootstrap.min.js',
              'style.css',
              'favicon.png']
#OPTIONS = {'argv_emulation': True, "resources":["index.html"]}
OPTIONS = {
  'argv_emulation': True,
  'iconfile':'favicon.png'
}

setup(
    name='charactr',
    py_modules=['contacts','chat_to_csv','imsg_stats', 'time_chart',
    'helpers/__init__','helpers/utils'],
    version='0.2',
    description='Visualizing your iMessage data',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
