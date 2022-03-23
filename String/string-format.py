var="Tom"
num=3
my_string="the variable is %s" % var # we have a placeholder with a string here 
# then afterwards we fill the placeholder with our string here
print(my_string)
my_num="The number is %d" % num
float_num=3.123
my_float="the float is %f" % float_num
print(my_float)
my_pres="The precision is %.2f" % float_num # only 2 point
print(my_pres)
# new styles
float_num_two=6.433123123
my_pres_two="The precision is {:.3f} and {:.4f}".format(float_num,float_num_two)
print(my_pres_two)
#another way
my_pres_three=f"The precision is {float_num} and {float_num_two}"
print(my_pres_three)