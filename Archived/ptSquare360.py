from turtle import *

def main():
    wn = Screen()
    tt1 = Turtle()
    tt1.hideturtle()
    tt1.speed('fastest')
    tt1.color ('blue')
    length = 150
    turnMain = 90
    turnSmall = 10
    for b in range (5):
        for a in range(36):
            tt1.fd(length)
            tt1.right(turnMain)  # turn right
            tt1.forward(length)
            tt1.right(turnMain)
            tt1.forward(length)
            tt1.right(turnMain)
            tt1.forward(length)
            tt1.right(turnMain)
            tt1.right(turnSmall)
        length += 10
      
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