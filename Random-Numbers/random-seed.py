import random
# The seed() method is used to initialize the random number generator.

# The random number generator needs a number to start with (a seed value), to be able to generate a random number.

# By default the random number generator uses the current system time.

# Use the seed() method to customize the start number of the random number generator.

# Note: If you use the same seed value twice you will get the same random number twice. See example below
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))