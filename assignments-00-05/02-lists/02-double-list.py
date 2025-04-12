def double_list() -> list[int]:
  numbers:list = [1,6,8,3]
  
  for i in range(len(numbers)):
    store_list_of_numbers = numbers[i]
    numbers[i] = store_list_of_numbers * 2

  print(numbers)

double_list()

 # output -> [2,12,16,6]