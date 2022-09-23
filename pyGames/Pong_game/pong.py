import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Rafa")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid =5, stretch_len=1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid =5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = 0.18

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier New", 26, "normal"))



def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
     
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)        
    
# kb bind
wn.listen()
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")
     

#Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("mixkit-game-ball-tap-2073.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("mixkit-game-ball-tap-2073.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 390:         
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier New", 26, "normal"))
        winsound.PlaySound("good-6081.wav", winsound.SND_ASYNC)
        
    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1  
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier New", 26, "normal"))
        winsound.PlaySound("good-6081.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() >= paddle_b.ycor() - 30 and ball.ycor() <= paddle_b.ycor() + 30:
        ball.setx(340) 
        ball.dx *= -1
        winsound.PlaySound("mixkit-game-ball-tap-2073.wav", winsound.SND_ASYNC) 
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() >= paddle_a.ycor() - 30 and ball.ycor() <= paddle_a.ycor() + 30:
        ball.setx(-340) 
        ball.dx *= -1
        winsound.PlaySound("mixkit-game-ball-tap-2073.wav", winsound.SND_ASYNC)  