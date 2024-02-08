# E5-kEEP
import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    while True:
        focus_time = 60  # 专注时长设置为60分钟
        focus_timer(focus_time)
        print("\nTake a break! Starting next session in 60 minutes...\n")
        time.sleep(60 * 60)  # 等待60分钟后开始下一个专注时钟循环
