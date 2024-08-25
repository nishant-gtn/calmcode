# def power(n):
#     def func(number):
#         return number**n

#     return func


# pow2 = power(3)
# pow3 = power(2)

# print(pow2(2), pow3(3))


import time
import random


def stopwatch(f):
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"This function took: {time.time() - tic}")
        return result

    return func


def sleep_random(s=1):
    time.sleep(s + random.random())
    return "Done!"


timed_sleep = stopwatch(sleep_random)
timed_sleep(3)
