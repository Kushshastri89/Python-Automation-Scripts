import os
import time
from datetime import datetime


def shutdown_at_midnight():
    print("🕛 Shutdown scheduler started. PC will shut down at 12:00 AM every night.")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "00:00":
            print("⚠️ Time reached 12:00 AM. Shutting down...")
            if os.name == 'nt':  # Windows
                os.system("shutdown /s /t 1")
            else:  # Linux or macOS
                os.system("sudo shutdown now")
            break  # Exit loop after shutdown command issued

        time.sleep(30)  # Check every 30 seconds


if __name__ == "__main__":
    shutdown_at_midnight()
