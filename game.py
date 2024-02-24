#Yazan Yiğit çıtak

import turtle
import random
import time
import tkinter as tk
import data
import degiskenler as veri


def oyun1():
        screen = turtle.Screen()
        screen.title("konsol Y - YILAN OYUNU")
        screen.setup(width=700, height=700)
        screen.tracer(0)
        screen.bgcolor("#1d1d1d")


        turtle.speed(1)
        turtle.pensize(4)
        turtle.penup()
        turtle.goto(-310,250)
        turtle.pendown()
        turtle.color("red")
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.penup()
        turtle.hideturtle()

        try:
            puan_file = open("puan.txt","r")
            puan_veri = puan_file.write()
            puan_veri_int = int(puan_veri)
            score = puan_veri_int;
            delay = 0.1

        except:
            score = 0;
            delay = 0.1


        snake = turtle.Turtle()
        snake.speed()
        snake.shape("square")
        snake.color("blue")
        snake.penup()
        snake.goto(0,0)
        snake.direction ='stop' 


        fruit = turtle.Turtle()
        fruit.speed(0)
        fruit.shape("square")
        fruit.color("white")
        fruit.penup()   
        fruit.goto(30,30)

        old_fruit = []

        scoring = turtle.Turtle() 
        scoring.color("white")
        scoring.penup()
        scoring.hideturtle()
        scoring.goto(0,300)
        scoring.write("Score: ", align="center", font=("Courier",24,"bold"))


        def snake_go_up():
            if snake.direction != "down":
                snake.direction = "up"

        def snake_go_down():
            if snake.direction != "up":
                snake.direction = "down"

        def snake_go_left():
            if snake.direction != "right":
                snake.direction = "left"

        def snake_go_right():
            if snake.direction != "left":
                snake.direction = "right"

        def snake_move():
            if snake.direction == "up":
                y = snake.ycor()
                snake.sety(y + 20)
            if snake.direction == "down":
                y = snake.ycor()
                snake.sety(y - 20)
            if snake.direction == "left":
                x = snake.xcor()
                snake.setx(x - 20)
            if snake.direction == "right":
                x = snake.xcor()
                snake.setx(x + 20)


        screen.listen()
        screen.onkeypress(snake_go_up, "Up")
        screen.onkeypress(snake_go_down, "Down")
        screen.onkeypress(snake_go_left, "Left")
        screen.onkeypress(snake_go_right, "Right")


        while True:
            screen.update()

            if snake.distance(fruit) < 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x,y)
                scoring.clear()
                score += 1
                scoring.write("Score: {}".format(score), align="center", font=("Courier", 24,"bold"))
                delay -= 0.001

                
                
                #lvl_file = open("puan.txt","w")
                #lvl_veri = lvl_file.write(str(score))
                #lvl_file.close()

                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape("square")
                new_fruit.color("green")
                new_fruit.penup()
                old_fruit.append(new_fruit)


            for index in range(len(old_fruit)-1, 0, -1):
                a = old_fruit[index -1].xcor()
                b = old_fruit[index -1].ycor()

                old_fruit[index].goto(a,b)

            if len(old_fruit) > 0:
                a = snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a, b)
            snake_move()


            if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("turquoise")
                scoring.goto(0,0)
                scoring.write("    Game Over \n Your score is {}".format(score), align="center", font=("Courier", 30,"bold"))


                for food in old_fruit:
                    if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor("turquoise")
                        scoring.goto(0, 0)
                        scoring.write("    Game Over \n Your score is {}".format(score), align="center",font=("Courier", 30, "bold"))

            time.sleep(delay)

        turtle.Terminator
        






def zar():
    def sayi():
        return random.randint(1, 9)


    def tek():
        for _ in range (1):
            print(sayi())
        print("------")

    def cift():
        for _ in range (2):
            print(sayi())
        print("------")



    pencere = tk.Tk()
    pencere.minsize(450,250)
    pencere.title("Zar programı")

    boyut = "40"

    tek_button = tk.Button(pencere,text="Tek zar",command=tek,font=f"italic {boyut}")
    tek_button.pack()

    cift_button = tk.Button(pencere,text="Çift zar",command=cift,font=f"italic {boyut}")
    cift_button.pack()

    bosluk1 = tk.Label(pencere,text=" ")
    bosluk1.pack()


    bosluk2 = tk.Label(pencere,text=" ")
    bosluk2.pack()

    bosluk3 = tk.Label(pencere,text=" ")
    bosluk3.pack()

    alt_baslik = tk.Label(pencere,text="Yiğit Çıtak")
    alt_baslik.pack()



    pencere.mainloop()


def pencere():
    main_input_istek_mesaj = input(f"{veri.prgm}Pencerenin içine ne yazalım?\nYazılacak: >")
    data.data_yaz(main_input_istek_mesaj)

    istek_pencere = tk.Tk()
    istek_pencere.minsize(400,200)
    istek_pencere.title("Program")

    istek_mesaj = tk.Label(istek_pencere,text=main_input_istek_mesaj,font="italic 25")
    istek_mesaj.pack()


    istek_pencere.mainloop()

















               #/\
              #/  \
             #/    \
            #/      \
           #/        \
          #/          \
         #/ \         /\
        #/   \       /  \
       #/     \     /    \
      #/       \   /      \
     #/         \ /        \
    #/           |          \
   #/            |           \
  #/             |            \
 #/              |             \
#/______________________________\