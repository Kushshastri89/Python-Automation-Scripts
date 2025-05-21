import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # overwrite the same line
        time.sleep(1)
        t -= 1

def pomodoro(work=25*60, short_break=5*60, long_break=15*60, cycles=4):
    for i in range(1, cycles+1):
        print(f"Pomodoro {i}: Work for {work//60} minutes.")
        countdown(work)
        if i != cycles:
            print(f"Short break for {short_break//60} minutes.")
            countdown(short_break)
        else:
            print(f"Long break for {long_break//60} minutes.")
            countdown(long_break)
    print("Pomodoro sessions complete! Well done!")

if __name__ == "__main__":
    pomodoro()
