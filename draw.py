from turtle import Turtle,Screen


tim=Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.color("pink")
tim.pencolor("black")
def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)

def cl():

    tim.clear()
    tim.home()

screen=Screen()
screen.listen()
screen.onkey(move_forward ,key="Up")
screen.onkey(move_backward ,key="Down")
screen.onkey(counter_clockwise ,key="Left")
screen.onkey(clockwise,key="Right")
screen.onkey(cl ,key="c")





screen.exitonclick()



