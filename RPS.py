import random
from DetermineWinner import winner
from insult import insult

playerCounter = 0
computerCounter = 0

def action():
    possible_action = ["r","p","s"]    
    
    user_input =  input("Enter r, p, s \n")
    computer_action = random.choice(possible_action)
    printResult(user_input, computer_action)

def printResult(user_input, computer_action):
    global playerCounter, computerCounter
    result = winner(user_input, computer_action)   

    print("Player: ", playerCounter, " Computer: ", computerCounter)
    print("You chose: ",user_input,", computer chose: ",computer_action)
     
    if ( result== "Computer won"):  
        print("Computer won")
        computerCounter = computerCounter + 1
        print(insult())  

    elif result == "You won":
        playerCounter = playerCounter + 1
        print("Player Won")
        
    
    else:
        print("It's a tie!")

    tryAgain()

def tryAgain():
    play_again = input("\nDo you want to play again? Enter y or n ")

    if play_again == "y":
        action()
    else: 
        print("Bye Bye")