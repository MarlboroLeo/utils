import functools
import time


def sount_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        print("function %s: %.2f seconds" % (func.__name__, duration_time))
        return result
    return wrapper