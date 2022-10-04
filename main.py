
# ******************************
# Make your Code
# ******************************
import random

numbers = []

while len(numbers) < 10:
    numbers.append(random.randint(0,100))


smallest = min(numbers)
print(smallest)
print(numbers.index(smallest))