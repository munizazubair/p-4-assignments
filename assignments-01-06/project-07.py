import random

print("Welcome to Your Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+[]{}|;:,.<>?"

number = int(input("How many passwords do you want to generate? "))
length = int(input("Enter the length of the password: "))

print("\nHere are your passwords:")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)