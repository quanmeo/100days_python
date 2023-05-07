import string
import random


print('Welcome to the PyPassword Generator')
num_letters= int(input('How many letters would you like in your password?\n'))
num_symbol = int(input('How many symbols would you like?\n'))
num_digit = int(input('How many numbers would you like?\n'))

ret = []
ret = random.sample(string.ascii_lowercase, num_letters) + random.sample(string.punctuation, num_symbol) + random.sample(string.digits, num_digit)

random.shuffle(ret)

print(f"Here is your password: {''.join(ret)}\n")
