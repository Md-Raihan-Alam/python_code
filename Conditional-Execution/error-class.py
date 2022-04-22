# error class
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x>100:
        raise ValueTooHighError("Value is too high")
    else:
        print('Ok')

try:
    test_value(132)
except ValueTooHighError as e:
    print(e)
finally:
    print("Code ok")