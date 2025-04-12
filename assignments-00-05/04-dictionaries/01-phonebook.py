def manage_phone_numbers():

    phonebook = {}                  

    while True:
        name = str(input("Name: "))
        if name == "":
            break
        number = int(input("Number: "))
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):

    for name in phonebook:
        print(f"{(name)} -> {phonebook[name]}")
        
def lookup_numbers(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = manage_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

main()