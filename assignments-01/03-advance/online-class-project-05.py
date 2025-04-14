import random
import time

def naive_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def binary_search(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if array[midpoint] == target:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array, target, low, midpoint - 1)
    else:
        return binary_search(array, target, midpoint + 1, high)

if __name__ == "__main__":
    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length , 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", end - start , "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", end - start , "seconds")