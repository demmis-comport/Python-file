#ch02ex04.py
#도형 그리기 함수


import turtle as t



def moveT(x,y):
    t.up()
    t.goto(x,y)
    t.down()


def drawPoly(n, d, x, y):
    moveT(x,y)
    for i in range(n):
        t.forward(d)
        t.left(360/n)




moveT(100,100)
drawPoly(4,80,-100,-100)
