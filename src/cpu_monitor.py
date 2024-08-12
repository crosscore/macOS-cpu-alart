import psutil
import os

# 閾値の設定
threshold = 90  # %
required_consecutive_checks = 3  # 連続して条件を満たす回数
check_interval = 1  # 秒

# CPU 使用率をチェックする関数
def check_cpu_usage():
    consecutive_checks = [0] * psutil.cpu_count()  # 各コアの連続チェックカウンター

    while True:
        cpu_usage = psutil.cpu_percent(interval=check_interval, percpu=True)
        for i, usage in enumerate(cpu_usage):
            if usage > threshold:
                consecutive_checks[i] += 1
                if consecutive_checks[i] >= required_consecutive_checks:
                    print(f"Core {i} usage exceeded {threshold}% for {required_consecutive_checks} consecutive checks")
                    os.system('afplay /System/Library/Sounds/Glass.aiff')  # アラート音を鳴らす
                    consecutive_checks[i] = 0  # リセット
            else:
                consecutive_checks[i] = 0  # リセット

if __name__ == "__main__":
    check_cpu_usage()
