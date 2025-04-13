import random

NUM_ROUNDS = 3
SCORE = 0

print("Welcome to the High-Low Game!")
def high_low_game(user_num, com_num, user_input):
    if user_num > com_num and user_input == "higher":
        print("You were right! The computer's number was", com_num)
        return True
    elif user_num < com_num and user_input == "lower":
        print("You were right! The computer's number was", com_num)
        return True
    else:
        print("Aww, that's incorrect. The computer's number was", com_num)
        return False

def main():
    global SCORE
    for round_num in range(1, NUM_ROUNDS + 1):
        print("Round", round_num)

        user_num = random.randint(0, 100)
        com_num = random.randint(0, 100)

        print("Your number is:", user_num)
        user_input = input("Do you think Your number is higher or lower than the computer's? ").strip().lower()

        result = high_low_game(user_num, com_num, user_input)

        if result:
            SCORE += 1

        print("Your score is now:", SCORE)
        print("--------------------")

    print("Game Over! Your Final Score is:", SCORE)
    if SCORE == 0 or SCORE == 1:
      print("Better luck next time!")
    elif SCORE == 2:
      print("Good job, you played really well!")
    elif SCORE == 3:
      print("Wow! You played perfectly!")

main()
