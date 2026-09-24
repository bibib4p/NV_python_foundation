# Countdown
import time

start = int(input("Enter a number to count down from: "))
print("--- COUNTDOWN INITIATED ---")
for num in range(start, 0, -1):
    print(f"{num}", end = " ", flush = True)
    time.sleep(0.5)

print("\nLIFTOFF!")