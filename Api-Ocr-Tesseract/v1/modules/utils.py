from functools import wraps
import time

def cronometra(function):
    @wraps(function)
    def wrapper(*args, **kwrds):
        start = time.time()
        ret =  function(*args, **kwrds)
        end = time.time() - start
        print("INFO:     This is the time that took for", function.__name__, "to finish executing:", end)
        return ret
    return wrapper
