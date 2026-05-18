import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(1, nr_letters+1):
    password_letters = random.choice(letters)
    password += password_letters

for symbol in range(1, nr_symbols+1):
    password_symbols = random.choice(symbols)
    password += password_symbols

for number in range(1, nr_numbers+1):
    password_numbers = random.choice(numbers)
    password += password_numbers

print("Password: " + password)

# To create a complex password

shuffle_password = list(password)
random.shuffle(shuffle_password)
complex_password = " "
for char in shuffle_password:
    complex_password += char

print("Recommended Strong Password" + complex_password)

    
