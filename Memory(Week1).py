# implementation of card game - Memory

import simplegui
import random

turn = 0
num = []
state = 0
# helper function to initialize globals
def new_game():
    global lst, exposed, card1, card2, turn
    lst = range(8) + range(8)
    card1 = 0
    card2 = 0   
    random.shuffle(lst)
    turn = 0
    exposed = [False for i in range(len(lst))]

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turn, card1, card2
    p = pos[0] // 50
    if exposed[p] == False:
        if state == 0:
            state = 1
            card1 = pos[0] // 50
            exposed[card1] = True
        elif state == 1:
            card2 = pos[0] // 50
            if card1 != card2:
                exposed[card2] = True
                state = 2
                turn += 1
        elif state == 2:
            if lst[card1] != lst[card2]:
                exposed[card1] = False
                exposed[card2] = False
                state = 1
            card1 = pos[0] // 50
            if exposed[card1] == False:
                exposed[card1] = True
                state = 1

# cards are logically 50x100 pixels in size    
def draw(canvas):
    count = -1
    counts = 0
    #Draw secret num
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text(str(lst[i]), (50 * i + 10, 68), 52, 'White')
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i+50, 0),
                                 (50 * i+50, 100), (50 * i, 100)],
                                2, 'Red', 'Green')
    label.set_text('Turns: ' + str(turn))    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
