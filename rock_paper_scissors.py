import random
def play_game():
    player_score = 0
    computer_score = 0

    while True:
       user_action = input("Enter a choice (rock, paper, scissors):").lower()
       possible_actions = ["rock", "paper", "scissors"]
       computer_action = random.choice(possible_actions)
       print(f"\nYou choose{user_action}, computer chose{computer_action}.\n")
    # Game logic
       if user_action == computer_action:
           print("It's a tie!")
       elif (user_action == "rock" and computer_action == "scissors") or \
            (user_action == "paper" and computer_action == "rock") or \
            (user_action == "scissors" and computer_action == "paper"):
          print("You win!")
          player_score +=1
       else:
           print("You lose!")
           computer_score +=1

       print(f"\nScore You:{player_score}| Computer: {computer_score}")

       if player_score == 3:
           print("You won the match!")
           break

       if computer_score == 3:
           print("computer won the match!")
           break

       replay = input("\nPlay Again? (yes or no):").lower()

       if replay != "yes":
            print("Final Score:")
            print(f"You: {player_score}| Computer: {computer_score}")
            print("Thanks for playing!")
            break
         
if __name__ == "__main__":
    play_game()
    
