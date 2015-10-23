# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
# helper functions
def name_to_number(name):
    """
    Convert name to number for RPSLS game
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

def number_to_name(number):
    """
    Convert number to name for RPSLS game
    """
    return {
        0: 'rock',
        1: 'Spock',
        2: 'paper',
        3: 'lizard',
        4: 'scissors',
        5: 'Error parameter'
    }.get(number, 5)

def rpsls(player_choice): 
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    assert player_number != None
    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(computer_number)
    # print out the message for computer's choice
    print "Computer chooses " + computer_choice
    # compute difference of comp_number and player_number modulo five
    game_dif = (computer_number  - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if game_dif == 1 or game_dif == 2:
        print "Computer wins"
    elif game_dif == 3 or game_dif == 4:
        print "Player wins"
    else:
        print "Player and computer tie!"
    print "\n"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


