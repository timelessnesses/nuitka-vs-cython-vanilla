import time
import datetime


def loop():
    for x in range(10000):
        yield x


def test():
    start = time.time()
    for x in loop():
        print(f"{x+1} loops passed", end="\r")
    result = time.time() - start
    print(f"\nUsed {str(datetime.timedelta(seconds=result))}", end="")
