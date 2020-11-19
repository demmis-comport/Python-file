import turtle as t

t.bgcolor('black')
t.speed(0)

color=('red','yellow','blue')

for x in range(200):
    t.color(color[x%3])
    t.forward(x*2)
    t.left(119)
