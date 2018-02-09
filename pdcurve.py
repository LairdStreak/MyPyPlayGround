from turtle import *

def main():
    wn = Screen()
    tt1 = Turtle()
    tt1.hideturtle()
    tt1.speed('fastest')
    tt1.color ('blue')
    for a in range(400):
        x = a
        y = 400 - x
        drawLine(tt1, x, 0, 0, y)
    tt1.color ('gold4')
    drawLine (tt1, -200, -10, 325, -10)
    drawLine (tt1, -200, -15, 325, -15)
    wn.exitonclick()

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
    ttl.penup()
    ttl.goto (x1, y1)
    ttl.pendown()
    ttl.goto (x2, y2)
    ttl.penup()



if __name__ == '__main__':
    main()