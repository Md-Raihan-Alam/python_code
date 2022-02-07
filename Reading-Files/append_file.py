# a=add or append new line
file = open("Sample_two.txt", "a")
roll = input("Enter Roll:")
name = input("Enter Name:")
line = "Roll="+str(roll)+" Name="+str(name)
file.write(line)
file.close()
