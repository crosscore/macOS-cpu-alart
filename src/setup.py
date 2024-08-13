from setuptools import setup

APP = ['cpu_monitor.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['psutil'],
    'plist': {
        'LSUIElement': True,
    },
    'frameworks': ['Cocoa'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
