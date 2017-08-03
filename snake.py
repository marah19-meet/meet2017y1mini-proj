import turtle
import random
turtle.fillcolor("yellow")
wn=turtle.Screen()
wn.bgcolor("black")


turtle.tracer(1,0)
turtle.register_shape("trash.gif") 
food = turtle.clone()
food.shape("trash.gif")
food.penup()


SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH =8

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
snake = turtle.clone()
snake.shape("circle")
turtle.hideturtle()


for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamps = snake.stamp()
    stamp_list.append(stamps)

UP_ARROW = "Up"
LEFT_ARROW = "Left"  
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 150
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
    move_snake()
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



def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
   
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    stamp = food.stamp()
    food_stamps.append(stamp)




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
    pos_list.pop(0)
    snake.clearstamp(old_stamp)
    
    
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind]) 

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        pos_list.pop(0)
        make_food()
        new_stamp=turtle.stamp()
        food_stamps.append(new_stamp)
        
        #HINT: This if statement may be useful for Part 8 

        

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
    if pos_list[-1] in pos_list[:-1]:
        print("you ate yourself")
        quit()
        
        
        


        
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
make_food()

turtle.mainloop()



##food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
##food_stamps = []
##for this_food_pos in food_pos:
##    x_pos= this_food_pos[0]
##    y_pos= this_food_pos[1]
##    food.goto(x_pos,y_pos)
##    stamp_id=food.stamp()
##    food_stamps.append(stamp_id)
food.hideturtle()


