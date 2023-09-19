# importing library
import turtle

# screen
sc = turtle.screen()
sc.tittle("pong game")
sc.bgcolor("white")
sc.setup(width=100, height=600)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle. Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.penup()
left_pad.goto(400, 0)

#ball of square
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("square")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# initilazie the score 
left_player = 0
right_player = 0

# display the score 
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("left_player : 0      right_player : 0", 
             aligne="center", font=("courier", 24, "normal"))

# Functions to move paddle Vertical
def paddleaup():
y = left_pad.ycor
y += 20
left_pad.sety(y) 

def paddleadown():
    y = left_pad.ycor()
    y-= 20
    left_pad.sety(y)

   def paddlebup():
   y = left_pad.ycor
   y += 20
   left_pad.sety(y) 

   def paddlebdown():
    y = right_pad.ycor
    y -= 20
    right_pad.sety(y)

    # Keyboard bindings 
    sc.list
    sc.onkeypress(paddleaup, "e")
    sc.onkeypress(paddleadown, "x")
    sc.onkeypress(paddlebup, "Up")
    sc.onkeypress(paddlebdown, "Down")

    while True:
       sc.update()

       hit_ball.setx(hit_ball.xcore()+hit_ball.dx)
       hit_ball.setx(hit_ball.xcore()+hit_ball.dy)

       
       # Checking boarders 
       if hit_ball.ycor() > 280:
          hit_ball.sety(280)
          hit_ball.dy *= -1

          if hit_ball.ycor() < -280:
             hit_ball.sety(-280)
             hit_ball.dy *= -1:

             if hit_ball.xcore() > 500:
                hit_ball.goto(0, 0)
                hit_ball.dy *= -1
                left_player += 1
                sketch.clear()
                sketch.write("Left_player : {}   Right_player: {}". format(
                   left_player, right_player), aligne="center",
                   font=("Courier", 24, "normal"))
                
                if hit_ball.xcore( ) < -400:
                   hit_ball.goto(0, 0)
                   hit_ball.dy *= -1 
                   right_player += 1
                   sketch.clear()
                   sketch.write("Left_player : {}   Right_player: {}". format(
                   left_player, right_player), aligne="center",
                   font=("Courier", 24, "normal"))

                   # Paddle ball colition
                   if (hit_ball.xcor() > 360 and 
                       hit_ball.xcor() <  370) and (
                          hit_ball.ycor() < right_pad.ycor()+40 and 
                          hit_ball.ycor() > right_pad.ycor()-40):
                      
                      hit_ball.setx(360)
                      hit_ball.dx*=-1
                      
                      if (hit_ball.xcor() <-360 and hit_ball.xcor() <  -370) and (
                          hit_ball.ycor() < right_pad.ycor()+40 and 
                          hit_ball.ycor() > right_pad.ycor()-40):
                         
                         hit_ball.setx(-360)
                         hit_ball.dx*=-1