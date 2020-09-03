import turtle
import time
import random

delay = 0.1

# ate rate
ate = 0
topaterate = 0

# play field
window = turtle.Screen()
window.title("Pysnakegame by @shohan")
window.bgcolor("blue")
window.setup(width=650, height=650)
window.tracer(0)

# lets make the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 50)

segments = []

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Ate: 0  Top Ate Rate: 0", align="center", font=("Courier", 24, "normal"))

# adding function
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
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
#game loop
while True:
    window.update()

    # touch the border and u r dead

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment/body
        segments.clear()

        # reset the ate
        ate = 0

        # reset the ate
        delay = 0.1

        pen.clear()
        pen.write("Ate: {}  Top Ate Rate: {}".format(ate, topaterate), align="center", font=("Courier", 24, "normal"))


    if head.distance(food) < 20:
         #move the food randomly
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # make the snake grow
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        # minimizing the delay
        delay += 0.001

        # top ate rate
        ate += 10

        if ate > topaterate:
            topaterate = ate

        pen.clear()
        pen.write("Ate: {}  Top Ate Rate: {}". format(ate, topaterate),align="center", font=("Courier", 24, "normal"))

    # track the snake body
    for index in range(len(segments)-1, 0, -1):

        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # don't eat urself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment/body
            segments.clear()

            # reset the ate
            ate = 0

            # reset the ate
            delay = 0.1

            pen.clear()
            pen.write("Ate: {}  Top Ate Rate: {}".format(ate, topaterate), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)

window.mainloop()
