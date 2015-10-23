# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

secret_number = 0
secret_range = 100
secret_guess_remained = 0
# helper function to start and restart the game
def new_game():
    """
    Starts new game
    """
    global secret_number 
    global secret_guess_remained
    secret_number = random.randrange(0, secret_range)
    secret_guess_remained = int(math.ceil(math.log(secret_range + 1, 2)))
    print "New game. Range is [0,",secret_range,")"
    print "Number of remaining guesses is", secret_guess_remained
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game     
    global secret_range
    secret_range = 100;
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_range
    secret_range = 1000;
    new_game()
    
def input_guess(guess):
    """
    Handler for guess input
    """
    global secret_guess_remained
    int_value = int(guess)     
    print "Guess was", int_value 
    
    secret_guess_remained -= 1
    print "Number of remaining guesses is", secret_guess_remained
    if secret_guess_remained:
        #"Higher", "Lower", or "Correct".
        if secret_number > int_value:
            print "Higher!\n"
        elif secret_number < int_value:
            print "Lower!\n"
        else:
            print "Correct!\n"
            new_game()
    else:
        print "You ran out of guesses.  The number was", secret_number,"\n"
        new_game()
    

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("Hello, let's play a game", [5,100], 30, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess the number", 300, 200)
frame.add_input('Your guess', input_guess, 200)
frame.add_button("Range is [0,100)",range100, 200)
frame.add_button("Range is [0,1000)",range1000, 200)
frame.set_draw_handler(draw)

# call new_game 
new_game()

# Start the frame animation
frame.start()




# always remember to check your completed program against the grading rubric
