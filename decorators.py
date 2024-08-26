# def power(n):
#     def func(number):
#         return number**n

#     return func


# pow2 = power(3)
# pow3 = power(2)

# print(pow2(2), pow3(3))


import time
import random
from logger import logger


def stopwatch(f):
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"This function took: {time.time() - tic}")
        return result

    return func


def sleep_random(s=1):
    try:
        0 / 0
        logger.warning(f"This is a test line for logger with sleep value {s}")
        sleepAmount = s + random.random()  # nosec
        time.sleep(sleepAmount)
        return "Done!"
    except BaseException:
        logger.error("An error occurred", exc_info=True)


timed_sleep = stopwatch(sleep_random)
timed_sleep(3)
