import sys
import os

app_path = '/Applications/cpu_monitor.app/Contents/Resources/lib/python3.9/site-packages'
sys.path.append(app_path)

try:
    import psutil
    print("psutil is successfully imported.")
except ImportError as e:
    print(f"Failed to import psutil: {e}")
    print("Checking if psutil is in the app bundle:")
    if os.path.exists(os.path.join(app_path, 'psutil')):
        print("psutil directory found in the app bundle.")
    else:
        print("psutil directory not found in the app bundle.")
