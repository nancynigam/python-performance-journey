import time
import math

def do_heavy_math(n):
    total = 0
    for i in range(1, n):
        total += math.sqrt(i) * math.sin(i)
    return total

def waste_time_with_sleep(n):
    for _ in range(n):
        time.sleep(0.01)  # 10 ms each

def mixed_work():
    for _ in range(50):
        do_heavy_math(5_000)
        waste_time_with_sleep(5)

def main():
    while True:
        mixed_work()

if __name__ == "__main__":
    main()
