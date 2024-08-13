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
        self.consecutive_checks = [0] * psutil.cpu_count()
        self.font = {"family": "Menlo", "size": 12}  # 固定幅フォントを指定

    @rumps.timer(check_interval)
    def check_cpu_usage(self, _):
        cpu_usage = psutil.cpu_percent(interval=None, percpu=True)
        for i, usage in enumerate(cpu_usage):
            if usage > threshold:
                self.consecutive_checks[i] += 1
                if self.consecutive_checks[i] >= required_consecutive_checks:
                    self.alert(f"Core {i} usage exceeded {threshold}% for {required_consecutive_checks} consecutive checks")
                    os.system('afplay /System/Library/Sounds/Glass.aiff')
                    self.consecutive_checks[i] = 0  # リセット
            else:
                self.consecutive_checks[i] = 0  # リセット

        # Update menu bar title with overall CPU usage, right-aligned with space padding
        overall_usage = psutil.cpu_percent(interval=None)
        usage_str = f"{overall_usage:.1f}".rjust(5)  # 5 characters total (including decimal point)
        self.title = f"CPU: {usage_str}%"

if __name__ == "__main__":
    CPUMonitorApp().run()
