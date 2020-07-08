import turtle
import time
import keyboard
import cv2
import numpy as np

backgroud_imag = 'maze.gif'
gif = cv2.VideoCapture(backgroud_imag)
ret, frame = gif.read()

image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print(image.shape)
kernel = np.ones((9, 9), np.uint8)
# cv2.imshow("oroiginal image",image)
erosion = cv2.erode(image, kernel, iterations=1)
# cv2.imshow("Erroded image",erosion)
# cv2.waitKey()

height, width = image.shape

level = int(input("What level should u want to play 1 or 2 ? "))

boundry = []
for i in range(height):
   for j in range(width):
       if erosion[i, j] < 150:
           boundry.append([j - int(width / 2), -1 * i + int(height / 2)])

t = turtle.Turtle(shape="turtle")
t.fillcolor("blue")
t.penup()
t.pencolor("blue")

s = turtle.Screen()
s.setup(width, height)
s.bgpic(backgroud_imag)

t.speed(0)
t.goto(-5.45, -300)
t.pendown()
for aColor in ["yellow", "red", "purple", "blue"]:
   t.color(aColor)
   t.backward(40)
   t.left(90)
   t.hideturtle()
t.penup()
t.showturtle()

t2 = turtle.Turtle()
t2.speed(0)
t2.hideturtle()
t2.penup()
t2.goto(6, 210)
t2.pendown()
t2.dot(16, "green")
print(t2.pos())

t3 = turtle.Turtle()
t3.speed(0)
t3.hideturtle()
t3.penup()
t3.goto(200, 210)
t3.pendown()
t3.dot(16, "red")
print(t3.pos())

t4 = turtle.Turtle()
t4.speed(0)
t4.hideturtle()
t4.penup()
t4.goto(-200, -210)
t4.pendown()
t4.dot(16, "yellow")
print(t4.pos())

t5= turtle.Turtle()
t5.speed(0)
t5.shape("square")
t5.color("white")
t5.penup()
t5.hideturtle()
t5.goto(250, 250)



def goto_game():

   step_forward = 1
   step_angle = 1
   flag = "P"

   origin = [-40, 0]

   def goto_home():
       t.goto(origin)

   def blink(num, delay):
       while num:
           t.fillcolor("red")
           time.sleep(delay)
           t.fillcolor("blue")
           time.sleep(delay)
           num -= 1

   goto_home()
   while True:
       # print(keyboard.read_key(), " key was pressed.")
       if keyboard.is_pressed("up"):
           flag = "F"
       if keyboard.is_pressed("down"):
           flag = "B"
       if keyboard.is_pressed("right"):
           flag = "R"
       if keyboard.is_pressed("left"):
           flag = "L"
       if keyboard.is_pressed("space"):
           flag = "P"
       if keyboard.is_pressed("esc"):
           break
       if keyboard.is_pressed("b"):
           blink(2, 0.1)

       # print("flag is :",flag)

       # MOIVING OR STOPING THE TURTLE
       if flag == "F":
           t.forward(step_forward)
       elif flag == "B":
           t.backward(step_forward)
       elif flag == "R":
           t.right(step_angle)
       elif flag == "L":
           t.left(step_angle)
       elif flag == "P":
           t.forward(0)

       pos = [int(t.pos()[0]), int(t.pos()[1])]
       """if pos in boundry:
           t.forward(0)
           blink(5,0.1)
           t.hideturtle()
           goto_home()
           t.showturtle()
           flag="P"
           """

       for i in range(-310, -280, 1):
           for j in range(-40, 5, 1):
               if pos == [j, i]:
                   print("***YOU ARE WINNER***")
                   s1 = turtle.Screen()
                   s1.setup(500, 500)
                   s1.bgpic("index.png")

       for i in range(203, 215):
           for j in range(0, 14, 1):
               if pos == [j, i]:
                   t.fillcolor("green")
                   t2.clear()

       for i in range(203, 215):
           for j in range(196, 207, 1):
               if pos == [j, i]:
                   t.fillcolor("red")
                   t3.clear()

       for i in range(-215, -204):
           for j in range(-207, -196, 1):
               if pos == [j, i]:
                   t.fillcolor("yellow")
                   t4.clear()








       # print(type(boundry))

   print("****WE ARE OUT OF THE LOOP****")

   s.exitonclick()


if level == 1:
   t.speed(5)

   goto_game()

elif level == 2:
   t.speed(0)
   goto_game()
else:
   print("OOPs WrOnG InPuT!! \n Try Again")

