def double(num: int) -> int:
  
  return num * 2 

def main():
  
  num = int(input("Enter a number: "))
  num_double = double(num)
  
  print("Double that is: " , num_double)

main()