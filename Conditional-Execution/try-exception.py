try:
    a=5/0
except Exception as e:
    print(e)
# determine type error like below
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
finally:
    print("Run no matter what")