# Step 1: Initialize a List
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 2: Accessing Elements
def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range."

# Step 3: Modifying Elements
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} changed to '{new_value}'."
    else:
        return "Index out of range."

# Step 4: Slicing the List
def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Start or end index out of range."
    return lst[start:end]

# Step 5: Game Interaction
def main():
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Invalid index values.")

        elif choice == "4":
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

main()
