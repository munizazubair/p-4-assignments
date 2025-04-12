def main():
    count_dict = {} 
    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":
            break

        num = int(num) 
        
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for number in count_dict:
        print(f"{number} appears {count_dict[number]} times.")

main()
