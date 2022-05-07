def stat_dec_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

#syntax
# @mydecorator
# def dosomething():
#     pass

@stat_dec_decorator
def print_name():
    print('Alex')

# print_name=stat_dec_decorator(print_name)
print_name()