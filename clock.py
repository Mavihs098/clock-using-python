import turtle
import time
import datetime

clock = turtle.Screen()
clock.title("Analog Clock")
clock.bgcolor("White")
clock.setup(width=600, height=600)
clock.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")


pen.speed(0)              
pen.penup()               
pen.goto(0, -300)         
pen.pendown()             
pen.width(3) 
pen.fillcolor("black")    
pen.circle(300)
pen.penup() 
pen.goto(0,-4)  
pen.pendown()
pen.width(6)
pen.circle(4) 

for i in range(1,13):
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    pen.right(i*30)
    pen.forward(280)
    pen.pendown()
    pen.width(2)
    pen.forward(20)
    
for j in range(72):    
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    pen.right(j*5)
    pen.forward(290)
    pen.pendown()
    pen.width(2)
    pen.forward(10)

for k in range(1,13):
    pen.penup()
    pen.goto(0,-19)
    pen.setheading(90)
    pen.right(k*30)
    pen.forward(260)
    pen.pendown()
    pen.write(k, align="center", font=("Courier", 24, "normal"))      


               
    
    
    



turtle.done()