MAX_LENGTH = 3
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        item = lst.pop()
        print(item)

def main():
    lst = []
    while True:
        val = input("Enter a value: ")
        lst.append(val)
        if val == "":
            break
    print("Here is the list: ", lst)
    shorten(lst)
main()