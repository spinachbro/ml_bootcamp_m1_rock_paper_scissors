# Step 1 
import random
computer = random.choice(["rock", "paper", "scissors"])

# Step 2 
try:
    player = input("Choose rock, paper, or scissors: ").lower()
    
    if player not in ["rock", "paper", "scissors"]:
        raise ValueError("Invalid choice")
    
    print(f"You chose: {player} --- Computer chose: {computer}")
    
# Step 3
    if player == computer:
        print("Tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

except:
    print("Error: Enter rock, paper, or scissors only!")