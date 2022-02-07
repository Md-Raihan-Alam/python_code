# return is the END of function and return something
def greet():
    return "Hello"
print(greet()," Glen")
print(greet()," Sally")
# another example
def greetLang(lang):
    if lang=='fr':
        return "Bonjour"
    elif lang=="es":
        return "Hola"
    else:
        return "Hello"
print(greetLang("es")," Glen")
print(greetLang("fr")," Glen")
print(greetLang("en")," Glen")
# another example
def addTwo(a,b):
    added=a+b
    return added
print("The sum is ",addTwo(3,5))
