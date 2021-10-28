import random

password = []

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = list(map(str.upper, lower_case))
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(0, random.randint(0, 5)):
    password.append(random.choice(symbols))
for i in range(0, random.randint(0, 5)):
    password.append(random.choice(lower_case))
for i in range(0, random.randint(0, 5)):
    password.append(random.choice(upper_case))
for i in range(0, random.randint(0, 5)):
    password.append(random.choice(digits))

random.shuffle(password)
finalPass = ''.join(password)

print(f"Your random password is > R{finalPass}")
