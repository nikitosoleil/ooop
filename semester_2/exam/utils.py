import time
import functools


def timeit(f):
    @functools.wraps(f)
    def wrapper_timeit(*args, **kwargs):
        start = time.clock()
        result = f(*args, **kwargs)
        duration = time.clock() - start
        return result, duration

    return wrapper_timeit
