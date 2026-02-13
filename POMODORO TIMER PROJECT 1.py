import time

WORK_TIME = 1 * 60      # 25 minutes
SHORT_BREAK = 1 * 60    # 5 minutes
LONG_BREAK = 2 * 60    # 15 minutes


def countdown(seconds):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")


def pomodoro():
    cycles = 0

    while True:
        cycles += 1
        print(f"\n🍅 Work Session {cycles} – Stay focused!")
        countdown(WORK_TIME)

        if cycles % 4 == 0:
            print("\n😴 Long Break – Relax!")
            countdown(LONG_BREAK)
        else:
            print("\n☕ Short Break – Take a breath!")
            countdown(SHORT_BREAK)


pomodoro()