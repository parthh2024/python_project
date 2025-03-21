# importing turtle for graphics

import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Parth")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

# snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food .speed(0)
food .shape("circle")
food .color("red")
food .penup()
food .goto(0,100)

body = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="Center", font=("courier", 18 ,"normal"))

# function

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
     head.direction = "left"

def go_right():
    if head.direction != "left":
     head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+ 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y- 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x- 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+ 20)

# keyboard binding

wn.listen()
wn.onkeypress (go_up, "w")
wn.onkeypress (go_down, "s")
wn.onkeypress (go_left, "a")
wn.onkeypress (go_right, "d")

# main loop game 

while True:
    wn.update()

 # check for a collison with the border
    if head.xcor()>290 or head.xcor()<-290 or  head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    # hide the body
        for bodys in body :
            bodys.goto(1000, 1000)    

    # clearing the body  list
        body.clear()
     
     #reset the score
        score = 0
        #reset the delay
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="Center", font=("courier", 18 ,"normal"))

 
  #check for the collision with the food

    if head.distance(food) < 20:
        # move the food
        x = random.randrange(-280,280,20)
        y =random.randrange(-280,280,20)
        food.goto(x,y)

        # add agement
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        body.append(new_body)

        # speed up
        delay -=0.001

        #Increase the Score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="Center", font=("courier", 18 ,"normal"))



    # move the end segment first reverce order
    for index in range (len(body) -1 ,0 ,-1):
        x = body[index-1].xcor()
        y= body[index-1].ycor()
        body[index].goto(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)    

    move()

 #check for head collision with body
    for bodys in body:
        if bodys.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        #  hide the body
            for bodys in body :
                bodys.goto(1000, 1000)      
        
        # clearing the body  list  
            body.clear()  
        #reset the score
            score = 0 
        #reset the delay
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score), align="Center", font=("courier", 18 ,"normal"))


    time.sleep(delay)

wn.mainloop()

