from setuptools import setup

APP = ['cpu_monitor.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['psutil', 'rumps'],
    'plist': {
        'LSUIElement': True,
        'CFBundleIdentifier': 'com.yuu.cpumonitor',
        'NSHighResolutionCapable': True,
    },
    'resources': ['cpu_monitor.py'],
}

setup(
    app=APP,
    name='CPUMonitor',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['psutil', 'rumps'],
)
