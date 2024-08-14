# macOS-cpu-alart

## .appファイルの作成
```
python setup.py py2app
```


## 自動起動設定追加コマンド
```
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
</dict>
</plist>
```

## 自動起動設定削除用コマンド
```
launchctl unload ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
rm ~/Library/LaunchAgents/com.yuu.cpumonitor.plist
```
