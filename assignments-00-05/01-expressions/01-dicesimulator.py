import random
dice_sides: int = 6
def main():
    die_roll_1 = random.randint(1 , dice_sides)
    die_roll_2 = random.randint(1 , dice_sides)
    die_roll_3 = random.randint(1 , dice_sides)
    print(f"""~Rolling two dice 
          gets '{die_roll_1}' and '{die_roll_2}'
           and it's total '{die_roll_1 + die_roll_2}'""")
    print(f"""~Rolling three dice
           '{die_roll_1}, '{die_roll_2}' and '{die_roll_3}'
            and it's total '{die_roll_1 + die_roll_2 + die_roll_3}'""")
main()