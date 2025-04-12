import random
dice_sides :int = 6
def main():
    die_1 = random.randint(1, dice_sides)
    die_2 = random.randint(1, dice_sides)
    print(f"First Die : {die_1}")
    print(f"Second Die: {die_2}")
    print(f"Total of two dice: {die_1 + die_2}")
main()
