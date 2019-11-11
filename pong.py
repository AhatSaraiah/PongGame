#part1 : getting starting

import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Ahat")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) #stop the window from updating

#Score
score_left=0
score_right=0

#Left paddle 
paddle_l= turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("blue")
paddle_l.shapesize(stretch_wid=10,stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350,0)

#Right paddle 
paddle_r= turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("blue")
paddle_r.shapesize(stretch_wid=10,stretch_len=1)
paddle_r.penup()
paddle_r.goto(350,0)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=-2
ball.dy=-2

#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#function
def paddle_l_up():
    y=paddle_l.ycor()
    y+=20
    paddle_l.sety(y)

def paddle_l_down():
    y=paddle_l.ycor()
    y-=20
    paddle_l.sety(y)

def paddle_r_up():
    y=paddle_r.ycor()
    y+=20
    paddle_r.sety(y) 

def paddle_r_down():
    y=paddle_r.ycor()
    y-=20
    paddle_r.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_l_up,"w")
win.onkeypress(paddle_l_down,"s")
win.onkeypress(paddle_r_up,"Up")
win.onkeypress(paddle_r_down,"Down")

#main game loop
while True:
    win.update()
    
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,8)
        ball.dx*=-1
        score_left+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left,score_right),align="center",font={"courier",24,"normal"})

    if ball.xcor() < -390:
        ball.goto(0,8)
        ball.dx*=-1     
        score_right+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left,score_right),align="center",font={"courier",24,"normal"})


    #paddle and bak=ll collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() +40 and ball.ycor() > paddle_r.ycor() -40):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() +40 and ball.ycor() > paddle_l.ycor() -40):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
   