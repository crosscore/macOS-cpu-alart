# macOS-cpu-alart

## .appファイルの作成
```
python setup.py py2app
```

## .appファイルの移動
```
mv dist/cpu_monitor.app ~/Applications/
chmod +x ~/Applications/cpu_monitor.app/Contents/MacOS/cpu_monitor
```

## 自動起動設定追加コマンド
```
# ctrl+X, Y, Enter
nano ~/Library/LaunchAgents/com.yuu.cpumonitor.plist

chmod 644 ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
launchctl load ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
```

```com.yuu.cpumonitor.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yuu.cpumonitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/cpu_monitor.app/Contents/MacOS/cpu_monitor</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
        <key>PYTHONPATH</key>
        <string>/Library/Python/3.9/site-packages:/Library/Python/3.8/site-packages</string>
    </dict>
</dict>
</plist>
```

## 自動起動設定削除用コマンド
```
launchctl unload ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
killall cpu_monitor
rm ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
rm -rf ~/Applications/cpu_monitor.app
```
