def get_first_element(lst):
    print("First element in the list is:", lst[0])

def main():
    lst = []

    for i in range(1):
        element = input("Enter element : ")
        lst.append(element)

    get_first_element(lst)

main()
