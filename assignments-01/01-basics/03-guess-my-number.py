import random
def check():
  secret_num = random.randint(0,99)

  print("I am thinking of a number between 1 and 99..." , end="")

  guess_num = int(input("Enter a guess: "))
  while guess_num != secret_num:
    if guess_num > secret_num:
      print("Your guess is too high")
    else:
        print("Your guess is too low")

        secret_num = int(input("Enter a new number: "))
        print(f"Congrats! The number was: {str(guess_num)}")

check()