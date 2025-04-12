import math
def main():
  num_1 = int(input("Please enter an integer to be divided: "))
  num_2 = int(input("Please enter an integer to divide by: "))
  result = num_1 // num_2
  remainder = num_1 % num_2
  print(f"The result of this division is {result} with a remainder of {remainder}")
main()