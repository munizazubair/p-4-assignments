def get_list():
  lst = []
  while True:
    val = input("Enter a value: ")
    lst.append(val)
    if val == "":
      break

  print("Here is the list: " , lst)
get_list()