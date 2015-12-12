"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['imsg_stats.py']
DATA_FILES = ['index.html',
              'scatter2.html',
              'scatter2.js',
              'streamgraph/streamgraph.html',
              'streamgraph/streamgraph.js',
              'cross_filter/chart3.html',
              'cross_filter/chart3.js',
              'cloud/word_cloud.html',
              'cloud/word_cloud.js',
              'tree/word_tree.html',
              'tree/word_tree.html',
              'parallel/parallel.html',
              'parallel/parallel.js',
              'style.css']
#OPTIONS = {'argv_emulation': True, "resources":["index.html"]}
OPTIONS = {
  'argv_emulation': True
}

setup(
    name='pd_490',
    py_modules=['contacts','chat_to_csv','imsg_stats', 'time_chart',
    'cloud/word_cloud', 'tree/word_tree', 'helpers/__init__','helpers/utils'],
    version='0.3',
    description='Visualize your iMessage data',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
