import turtle
import time
import random

def setred(x):
    if x==1:
        red_light1.color("red")
    elif x==2:
        red_light2.color("red")
    elif x==3:
        red_light3.color("red")
    else:
        red_light4.color("red")


def setgreen(x):
    if x==1:
        green_light1.color("green")
    elif x==2:
        green_light2.color("green")
    elif x==3:
        green_light3.color("green")
    else:
        green_light4.color("green")

def setorange(x):
    if x==1:
        orange_light1.color("orange")
    elif x==2:
        orange_light2.color("orange")
    elif x==3:
        orange_light3.color("orange")
    else:
        orange_light4.color("orange")

t=5
a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
d=int(input("D:"))

l=5

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
FONT=("Arial",15,"normal","bold")
pen1._write(" A",align="center",font="FONT")

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
FONT=("Arial",15,"normal","bold")
pen2._write(" B",align="center",font="FONT")

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
FONT=("Arial",15,"normal","bold")
pen3._write(" C",align="center",font="FONT")


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
FONT=("Arial",15,"normal","bold")
pen4._write(" D",align="center",font="FONT")

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

#result box

box=turtle.Turtle()
box.color("red")
box.width(10)
box.write("......",align="center",font="FONT")

box1=turtle.Turtle()
box1.goto(0,0)
box1.color("black")
box1.width(80)
box1.fd(50)
box1.rt(180)
box1.fd(100)


while(True):
    if (a>0):
        red_light1.color("grey")
        if (a>=l):
            setgreen(1)
            box1.width(75)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)

            box.write("Road 1 is opened",align="center",font="FONT")
            a=a-l
            setred(2)
            setred(3)
            setred(4)
            time.sleep(t)
            print(t,"second in Line A")
            green_light1.color("grey")
            setorange(1)
            time.sleep(1)
            orange_light1.color("grey")
        else:
            m=t/a
            a=a-a
            setgreen(1)
            box1.width(70)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)

            box.write("Road 1 is opened",align="center",font="FONT")
            setred(2)
            setred(3)
            setred(4)
            time.sleep(m)
            print(m,"second in Line A")
            green_light1.color("grey")
            setorange(1)
            time.sleep(1)
            orange_light1.color("grey")    
    if(b>0):
        red_light2.color("grey")
        if (b>=l):
            setgreen(2)
            box1.width(80)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 2 is opened",align="center",font="FONT")
            b=b-l
            setred(1)
            setred(3)
            setred(4)
            time.sleep(t)
            print(t,"second in Line b")
            green_light2.color("grey")
            setorange(2)
            time.sleep(1)
            orange_light2.color("grey")
        else:
            m=t/b
            b=b-b
            setgreen(2)
            box1.width(80)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 2 is opened",align="center",font="FONT")
            setred(1)
            setred(3)
            setred(4)
            time.sleep(m)
            print(m,"second in Line B")
            green_light2.color("grey")
            setorange(2)
            time.sleep(1)
            orange_light2.color("grey")
    if(c>0):
        red_light3.color("grey")
        if (c>=l):
            setgreen(3)
            box1.width(90)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 3 is opened",align="center",font="FONT")
            c=c-l
            setred(1)
            setred(2)
            setred(4)
            time.sleep(t)
            print(t,"Second in junction c")
            green_light3.color("grey")
            setorange(3)
            time.sleep(1)
            orange_light3.color("grey")
        else:
            m=t/c
            c=c-c
            setgreen(3)
            box1.width(90)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 3 is opened",align="center",font="FONT")
            setred(1)
            setred(2)
            setred(4)
            time.sleep(m)
            print(m,"Second in Line C")
            green_light3.color("grey")
            setorange(3)
            time.sleep(1)
            orange_light3.color("grey")
    if (d>0):
        red_light4.color("grey")
        if (d>=l):
            setgreen(4)
            box1.width(100)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 4 is opened",align="center",font="FONT")
            d=d-l
            setred(1)
            setred(2)
            setred(3)
            time.sleep(t)
            print(t,"Second in Line D")
            green_light4.color("grey")
            setorange(4)
            time.sleep(1)
            orange_light4.color("grey")
        else:
            m=t/d
            d=d-d
            box1.width(100)
            box1.fd(100)
            box1.rt(180)
            box1.fd(100)
            box.write("Road 4 is opened",align="center",font="FONT")
            setgreen(4)
            setred(1)
            setred(2)
            setred(3)
            time.sleep(m)
            print(m,"Second in Line D")
            green_light4.color("grey")
            setorange(4)
            time.sleep(1)
            orange_light4.color("grey")
    a+=random.randint(1,5)
    b+=random.randint(1,5)
    c+=random.randint(1,5)
    d+=random.randint(1,5)
    print("End of Cycle\n\n")

    print("New Cycle")
    print("a=",a,"\nb=",b,"\nc=",c,"\nd=",d)



wn.mainloop()