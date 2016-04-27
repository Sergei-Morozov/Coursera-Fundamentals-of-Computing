# template for "Stopwatch: The Game"
# Hope you enjoy it xD
import simplegui
import math
# define global variables

counter = 0
win_count = 0
loss_count = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a_minutes = t // 600
    b_tenSeconds = (t//10) %60 // 10
    c_seconds = (t//10) %60 %10
    d_mseconds = t%10
    return str(a_minutes) +":"+ str(b_tenSeconds) + str(c_seconds) +"."+str(d_mseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global win_count, loss_count
    if timer.is_running():
        timer.stop()
        if counter%10:
            loss_count += 1
        else:
            win_count += 1
    
def reset():
    stop()
    global counter, win_count, loss_count
    
    counter = win_count = loss_count = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter),[140, 340], 48, "Red")
    canvas.draw_text("Hello, let's play a game", [75,75], 30, "Red")
    canvas.draw_text(str(win_count) + "/" + str(loss_count), [350,30], 30, "Red")
    
    #Easter egg
    canvas.draw_circle((200,200),100,10, "Red")
    ang = 270 + 36*(counter%10)
    dx = int(math.cos(math.radians(-ang))*100)
    dy = int(math.sin(math.radians(-ang))*100)
    canvas.draw_line((200,200),(200+dx,200-dy),5, "Red")


    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 400)
timer = simplegui.create_timer(100, timer_handler)
# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()

