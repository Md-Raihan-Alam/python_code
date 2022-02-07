def greet(lang):# lang is a parameter
    if lang=="es":
        print("Hola")
    elif lang=="fr":
        print("Bonjour")
    else:
        print("Hello")
greet("es")
greet("fr")
greet("en")
# another example
def sumOfTwo(a,b):
    sum=a+b
    print("The sum of ",a," and ",b," is ",sum)# do not add '+' if type of arguments is int
valueOne=input("Enter a number:")
valueIntOne=int(valueOne)
valueTwo=input("Enter another number:")
valueIntTwo=int(valueTwo)
sumOfTwo(valueIntOne,valueIntTwo)
