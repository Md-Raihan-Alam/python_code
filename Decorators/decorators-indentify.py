import functools
def stat_dec_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result
    return wrapper

@stat_dec_decorator
def add5(x):
    return x+5

print(help(add5)) #help->observe combine dump of built-in-function
print(add5.__name__)