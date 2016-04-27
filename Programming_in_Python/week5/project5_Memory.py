# implementation of card game - Memory

import simplegui
import random
game_list = []
exposed = [False for dummy_index in range(16)]
turns = 0
image = simplegui.load_image("http://media-hearth.cursecdn.com/attachments/2/101/cardback-rankedladder.png")
# helper function to initialize globals
def new_game():
    global game_list, state, turns, exposed
    game_list = range(0,8)
    game_list.extend(range(0,8))
    random.shuffle(game_list)
    exposed = [False for dummy_index in range(16)]
    turns = state = 0
    label.set_text("Turns = " + str(turns))

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, turns, first_index, second_index

    index = pos[0]//50

    if exposed[index]:
        return;
    exposed[index] = True
    
    if state == 0:
        state = 1
        first_index = index
        turns += 1

    elif state == 1:
        state = 2
        second_index = index
    else:
        state = 1
        turns += 1
        if game_list[first_index] != game_list[second_index]:
            exposed[first_index] = False
            exposed[second_index] = False
        first_index = index
    label.set_text("Turns = " + str(turns))

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    position = 0;
    position_increment = 800 // len(game_list)
    for index in range(len(game_list)):
        if exposed[index]:
            canvas.draw_text(str(game_list[index]), (position, 75), 90, 'Red')
        else:
            canvas.draw_polygon([(position, 0), (position + position_increment, 0), (position + position_increment, 100), (position, 100)],1, "Red", "Green")
            if image.get_width() !=0 and image.get_height() != 0:
                canvas.draw_image(image, (image.get_width()//2, image.get_height()//2), (image.get_width(), image.get_height()), (position+position_increment/2, 50), (50,100))
        position += position_increment


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))
label2 = frame.add_label("It takes time to load images :)")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric