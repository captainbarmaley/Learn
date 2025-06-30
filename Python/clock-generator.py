import time

clock = 0

while True:
    clock = 1 - clock # 1 0 1 0 1 0 ...
    print(f"Clock: {clock}")
    time.sleep(1) # sleep for 1 sec
