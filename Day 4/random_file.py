from random import *

# my_random = randint(1, 50)
# print(my_random)

# colors = ['Red', 'Blue', 'Green', 'White']
# my_random = choice(colors)
# print(my_random)

numbers = list(range(5, 50, 5))
shuffle(numbers)
print(numbers)
