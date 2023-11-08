import turtle as p
import colorsys

p.bgcolor('black')
p.tracer(10)
p.pensize(2)
h=0
n=40

for i in range(400):
    c=colorsys.hsv_to_rgb(h,0.9,1)
    p.width(i/100+2)
    p.pencolor(c)
    h +=1/n
    p.right(120)
    p.circle(-i*1, -100)
    p.circle(i*1, 100)
    p.circle(i*1, 60)

p.done()