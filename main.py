#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#list to create the password
password = []
# loop to get a random letter
for letter in letters:
  if nr_letters > 0:
    nr_letters -= 1
    x = random.randint(0, 51)
    password.append(letters[x])
    
for symbol in symbols:
  if nr_symbols > 0:
    nr_symbols -= 1
    x = random.randint(0, 8)
    password.append(symbols[x])

for number in numbers:
  if nr_numbers > 0:
    nr_numbers -= 1
    x = random.randint(0, 9)
    password.append(numbers[x])

#randomizing list
random.shuffle(password)
#making list into a string and printing
str1 = ""
for v in password:
  str1 += v
print(f'Your password is {str1}')

