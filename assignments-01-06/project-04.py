import random

def play():
    user = input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").strip().lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
print(play())