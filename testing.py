import time, datetime, random


def cython():
    start = time.time()
    import test3

    print("\nuse cython:", datetime.timedelta(seconds=time.time() - start), "\n")
    test3.test()


def nuitka():
    start = time.time()
    import test2

    print("\nuse nuitka:", datetime.timedelta(seconds=time.time() - start), "\n")
    test2.test()


def vanilla():
    start = time.time()
    import test

    print("\nuse vanilla:", datetime.timedelta(seconds=time.time() - start), "\n")
    test.test()


def main():
    tests = [cython, nuitka, vanilla]
    while len(tests) != 0:
        a = random.choice(tests)
        tests.remove(a)
        a()


if __name__ == "__main__":
    main()
