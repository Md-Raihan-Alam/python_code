from unittest.mock import NonCallableMagicMock


def talk(phrase):
    def say(word):
        print(word)
    
    words=phrase.split(' ')
    for word in words:
        say(word)

talk("I am going to buy the milk")

# 2nd example
def count():
    count=0
    def increment():
        nonlocal count
        #count will cause error without nonlocal cause increment
        # do not know count
        count=count+1
        print(count)
    increment()

count()