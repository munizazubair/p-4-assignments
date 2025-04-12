import math
def main():
  AB = float(input("Enter the length of AB: "))
  AC = float(input("Enter the length of AC: "))
  BC = math.sqrt(AB**2 + AC**2)         # math.sqrt => it's used to calculate the square root of a given number
  print(f"The length of BC (the hypotenuse) is: {BC}")

main()