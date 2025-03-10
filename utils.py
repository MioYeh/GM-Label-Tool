from functools import wraps
import time

def Timer(func):
    @wraps(func)
    def wrap(*args, **kargs):
        time_start = time.time()
        value = func(*args, **kargs)
        time_end = time.time()
        time_spend = time_end - time_start
        #print(f"[{func.__module__}.{func.__name__}] cost time: {time_spend}")
        print(f"[Timer][{func.__qualname__}] cost time: {time_spend}")

        return value

    return wrap