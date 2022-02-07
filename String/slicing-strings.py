user = "Md. Raihan Alam"
# slice is like "up to but not including"
# which means
print(user[0:4])
# 0 to 4 but do not include 4
print(user[6:7])
# 6 to 7 but do not include 7
print(user[6:20])
# 6 to 20 but do not include 20
# if you include more number like before code then it will not cause error

print(user[:2])
# means 0 (which will be default if no number is inputted) to  before 2
print(user[2:])
# means 2 to before end( default if end value is not given)
print(user[:])
# all input character
