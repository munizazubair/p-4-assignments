def add_three_copies(my_list, data):
  
  for i in range(3):
    my_list.append(data) # append => adds the data to the end of the list

def main():
  
  my_list = []

  print("List before" , my_list)

  data = input("Enter a message to copy ")
  add_three_copies(my_list, data)

  print("List after" , my_list)
  
main()