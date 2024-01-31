import random

# number = random.random()
# print(number)
# number = random.random() * 100
# print(number)

# number = random.randrange(20,35, 5)
# print(number)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
# print(numbers)
random_number = random.choice(numbers)
print(random_number)