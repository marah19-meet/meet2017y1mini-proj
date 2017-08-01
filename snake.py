import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0)#This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window #size.
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH =8
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    # You're RIGHT!
    x_pos=x_pos+SQUARE_SIZE#x+=1 its is also right
    my_pos=(x_pos,y_pos)#Store position variables in a tuple
    snake.goto(x_pos,y_pos)#Move snake to new(x,y)
    #Append the new position tuple to pos_list
    pos_list.append(my_pos)
    #Save the stamp ID! You'll need to erase it later. Then
    # append
    # it to stamp_list.
    stamps = snake.stamp()
    stamp_list.append(stamps)

UP_ARROW = "Up"
LEFT_ARROW = "Left"  
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100#Update snake position after this many
#milliseconds
SPACEBAR = "space"
UP = 0
LEFT=1
DOWN=2
RIGHT=3
direction=UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction 
    direction=UP 
    move_snake()#Update the snake drawing <- remember me later
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print("you pressed the down key")
def right():
    global direction
    direction=RIGHT
    print("you pressed the right key")
def left():
    global direction
    direction=LEFT
    print("you pressed the left key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

def move_snake():
    global direction
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("you moved UP")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("you moved down")
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos >=RIGHT_EDGE:
        print("you print the right edge,game over!")
        quit()
    elif new_x_pos<= LEFT_EDGE:
        print("you print the left edge,game over!")
        quit()
    elif new_y_pos>=UP_EDGE:
        print("you print the up edge,game over!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("you print the down edge,game over!")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()


turtle.register_shape("trash.gif") 
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in food_pos:
    x_pos= this_food_pos[0]
    y_pos= this_food_pos[1]
    turtle.goto(x_pos,y_pos)
    stamp.id=food.stamp
    food_stamps.append(stamp.id)


