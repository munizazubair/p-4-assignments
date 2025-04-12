TERM:int = 10000

def main():

  first_term:int = 0
  second_term:int = 1

  while first_term <= TERM:
    print(first_term)
    final_term = first_term + second_term
    first_term = second_term
    second_term = final_term
    
main()