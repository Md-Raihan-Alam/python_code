import functools
def stat_dec_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #DO...
        result=func(*args,**kwargs)
        #DO...
        return result
    return wrapper

@stat_dec_decorator
def add5(x):
    return x+5
