min_height:int = 40
max_height:int = 60

def main():
    height = input("Enter your height: ")

    while True:
      if height == "":
          height = input("Enter your height: ")
      else:  
        user_input = int(height)
        break  

    if user_input <= max_height and user_input >= min_height:
         print("You are tall enough to ride.")
    else: 
         print("You are not tall enough to ride.")

main()


