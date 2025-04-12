def addition_of_numbers(numbers):
    initial_number = 0
    for number in numbers:
        initial_number += number
    return initial_number

def sum_of_numbers():
    numbers: list[int] = [21, 92, 59, 74, 56, 12, 45, 78, 90, 100]
    sum = addition_of_numbers(numbers)
    print(sum)
sum_of_numbers()

 # output => 627