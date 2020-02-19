import turtle

a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
d=int(input("D:"))


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("C4F traffic system")

#BOX1
pen1=turtle.Turtle()
pen1.color("yellow")
pen1.hideturtle()
pen1.penup()
pen1.goto(-240,240)
pen1.pendown()
pen1.fd(60)
pen1.rt(90)
pen1.fd(120)
pen1.rt(90)
pen1.fd(60)
pen1.rt(90)
pen1.fd(120)


#BOX2
pen2=turtle.Turtle()
pen2.color("yellow")
pen2.hideturtle()
pen2.penup()
pen2.goto(240,240)
pen2.pendown()
pen2.fd(60)
pen2.rt(90)
pen2.fd(120)
pen2.rt(90)
pen2.fd(60)
pen2.rt(90)
pen2.fd(120)

#BOX3
pen3=turtle.Turtle()
pen3.color("yellow")
pen3.hideturtle()
pen3.penup()
pen3.goto(-240,-170)
pen3.pendown()
pen3.fd(60)
pen3.rt(90)
pen3.fd(120)
pen3.rt(90)
pen3.fd(60)
pen3.rt(90)
pen3.fd(120)



#BOX4
pen4=turtle.Turtle()
pen4.color("yellow")
pen4.hideturtle()
pen4.penup()
pen4.goto(240,-170)
pen4.pendown()
pen4.fd(60)
pen4.rt(90)
pen4.fd(120)
pen4.rt(90)
pen4.fd(60)
pen4.rt(90)
pen4.fd(120)


#Light1

red_light1 = turtle.Turtle()
red_light1.color("grey")
red_light1.shape("circle")
red_light1.penup()
red_light1.goto(-210,220)
red_light1.pendown()

orange_light1 = turtle.Turtle()
orange_light1.color("grey")
orange_light1.shape("circle")
orange_light1.penup()
orange_light1.goto(-210,180)
orange_light1.pendown()

green_light1 = turtle.Turtle()
green_light1.color("grey")
green_light1.shape("circle")
green_light1.penup()
green_light1.goto(-210,140)
green_light1.pendown()


#Light 2

red_light2 = turtle.Turtle()
red_light2.color("grey")
red_light2.shape("circle")
red_light2.penup()
red_light2.goto(267,220)
red_light2.pendown()

orange_light2 = turtle.Turtle()
orange_light2.color("grey")
orange_light2.shape("circle")
orange_light2.penup()
orange_light2.goto(267,180)
orange_light2.pendown()

green_light2 = turtle.Turtle()
green_light2.color("grey")
green_light2.shape("circle")
green_light2.penup()
green_light2.goto(267,140)
green_light2.pendown()


#Light 3

red_light3 = turtle.Turtle()
red_light3.color("grey")
red_light3.shape("circle")
red_light3.penup()
red_light3.goto(-210,-190)
red_light3.pendown()

orange_light3 = turtle.Turtle()
orange_light3.color("grey")
orange_light3.shape("circle")
orange_light3.penup()
orange_light3.goto(-210,-230)
orange_light3.pendown()

green_light3 = turtle.Turtle()
green_light3.color("grey")
green_light3.shape("circle")
green_light3.penup()
green_light3.goto(-210,-270)
green_light1.pendown()




#Light 4

red_light4 = turtle.Turtle()
red_light4.color("grey")
red_light4.shape("circle")
red_light4.penup()
red_light4.goto(267,-190)
red_light4.pendown()

orange_light4 = turtle.Turtle()
orange_light4.color("grey")
orange_light4.shape("circle")
orange_light4.penup()
orange_light4.goto(267,-230)
orange_light4.pendown()

green_light4 = turtle.Turtle()
green_light4.color("grey")
green_light4.shape("circle")
green_light4.penup()
green_light4.goto(267,-270)
green_light4.pendown()


wn.mainloop()
