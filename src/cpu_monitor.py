import psutil
import os
import rumps
import sys
import logging
import warnings

# pkg_resources の DeprecationWarning を抑制
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pkg_resources")

log_dir = '/Users/yuu/repos/macOS-cpu-alart/log'
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, 'cpu_monitor_debug.log')
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 閾値の設定
threshold = 90  # %
required_consecutive_checks = 3  # 連続して条件を満たす回数
check_interval = 3  # 秒

class CPUMonitorApp(rumps.App):
    def __init__(self):
        super(CPUMonitorApp, self).__init__("CPU")
        self.menu = []  # 初期化時にメニューを空にする
        self.consecutive_checks = 0
        self.font = {"family": "Menlo", "size": 12}  # 固定幅フォントを指定
        logging.info("CPUMonitorApp initialized")

    @rumps.timer(check_interval)
    def check_cpu_usage(self, _):
        try:
            cpu_usage = psutil.cpu_percent(interval=0.1, percpu=True)
            highest_usage = max(cpu_usage)

            # CPU使用率が閾値を超えた場合のみログを出力
            if highest_usage > threshold:
                self.consecutive_checks += 1
                logging.warning(f"High CPU usage detected: {highest_usage}% (Check {self.consecutive_checks}/{required_consecutive_checks})")

                if self.consecutive_checks >= required_consecutive_checks:
                    logging.critical(f"CPU usage exceeded {threshold}% for {required_consecutive_checks} consecutive checks")
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

        except Exception as e:
            logging.exception(f"Error in check_cpu_usage: {e}")

    def quit_app(self, _):
        logging.info("Quitting application")
        rumps.quit_application()

if __name__ == "__main__":
    logging.info("Starting CPU Monitor")
    app = CPUMonitorApp()
    app.run()
