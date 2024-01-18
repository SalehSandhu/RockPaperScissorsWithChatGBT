def winner(user_input, computer_action):   

    if user_input == computer_action:
        return "It's a tie!"
    elif user_input == "r":
        if computer_action == "p":
            return "Computer won"
        else:
            return "You won"

    elif user_input == "p":
        if computer_action == "s":
            return "Computer won"
        else:
            return "You won"
    
    elif user_input == "s":
        if computer_action == "r":
            return "Computer won"
        else:
            return "You won"