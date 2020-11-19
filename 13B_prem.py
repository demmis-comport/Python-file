#13B_prem.py
#
#거북이 이동하기

import turtle as t
def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()

t.shape('turtle')
t.speed(0)

t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(clear,"Escape")
t.listen()
