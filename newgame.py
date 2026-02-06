import turtle
import time
import random

delay=0.1
score=0
high_score=0

#window setup
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("white")
food.penup()
food.goto(0,100)

segment=[]

#score
pen=turtle.Turtle()
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

#main game loop
while True:
    wn.update()

    #check for border collisio with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for i in  segment:
            i.goto(1000,1000)
        #clear segments
        segment.clear()

        #reset score
        score=0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",24,"bold"))

        #reset delay
        delay=0.1

    #check for collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("pink")
        new_segment.penup()
        segment.append(new_segment)

        delay=delay-0.001

        #adding score
        score=score+1
        if score>high_score:
            high_score=score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",24,"bold"))

    #move the end segments first in reverse order
    for i in range (len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)


    #move segment 0 to where head is
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
    move()
    #check for collisions with head and bady
    for i in segment:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for i in segment:
                i.goto(1000,1000)
            
            segment.clear()

            #reset score
            score=0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",24,"bold"))

            #reset delay
            delay=0.1
            
    time.sleep(delay)

wn.mainloop()