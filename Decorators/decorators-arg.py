def stat_dec_decorator(func):
    def wrapper(*args,**kwargs):
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result
    return wrapper

@stat_dec_decorator
def add5(x):
    return x+5

result=add5(10)
print(result)