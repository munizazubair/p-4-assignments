
def main():
  year = int(input("enter a year: "))
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("It's a leap Year!")
      else:  
                print("It's not a leap Year")
    else:  
            print("It's a leap Year")
  else:  
        print("It's not a leap Year")
main()