import psutil
import os
import rumps

# 閾値の設定
threshold = 90  # %
required_consecutive_checks = 3  # 連続して条件を満たす回数
check_interval = 1  # 秒

class CPUMonitorApp(rumps.App):
    def __init__(self):
        super(CPUMonitorApp, self).__init__("CPU")
        self.menu = ["Quit"]
        self.consecutive_checks = 0
        self.font = {"family": "Menlo", "size": 12}  # 固定幅フォントを指定

    @rumps.timer(check_interval)
    def check_cpu_usage(self, _):
        cpu_usage = psutil.cpu_percent(interval=0.1, percpu=True)
        highest_usage = max(cpu_usage)

        # 最も使用率の高いコアの値が閾値を超えているかチェック
        if highest_usage > threshold:
            self.consecutive_checks += 1
            if self.consecutive_checks >= required_consecutive_checks:
                self.alert(f"CPU usage exceeded {threshold}% for {required_consecutive_checks} consecutive checks")
                os.system('afplay /System/Library/Sounds/Glass.aiff')
                self.consecutive_checks = 0  # リセット
        else:
            self.consecutive_checks = 0  # リセット

        # メニューバータイトルを更新
        usage_str = f"{highest_usage:.1f}".rjust(5)  # 5 characters total (including decimal point)
        self.title = f"CPU: {usage_str}%"

        # サブメニューに各コアの使用率を表示
        self.menu.clear()
        for i, usage in enumerate(cpu_usage):
            self.menu.add(rumps.MenuItem(f"Core {i}: {usage:.1f}%"))
        self.menu.add(None)  # セパレータを追加
        self.menu.add(rumps.MenuItem("Quit", callback=self.quit_app))

    def quit_app(self, _):
        rumps.quit_application()

if __name__ == "__main__":
    CPUMonitorApp().run()
