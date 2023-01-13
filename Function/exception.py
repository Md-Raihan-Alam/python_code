# try:
#     #some lines of code
#     raise Exception('An error')
# except <ERROR1>:
#     #handler<ERROR1>
# except <ERROR2>:
#     #handler<ERROR2>
# except: # all types error
#     #handle rest
# except Exception as error:
#     #custom error
# else:
#     # no exceptions were raised
# finally:
#     # do something in any case

try:
    result=2/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    result = 1
print(result)


class DogNotFoundException(Exception):
    print("error")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found")