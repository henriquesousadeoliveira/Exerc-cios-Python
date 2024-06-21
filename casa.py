import turtle

tata = turtle.Turtle()

x=100
tata.fillcolor("darkseagreen2")
tata.begin_fill()
for i in range(2):
    tata.forward(2*x)
    tata.left(90)
    tata.forward(x)
    tata.left(90)
tata.end_fill()

tata.forward(x/3)
tata.left(90)

tata.fillcolor("burlywood4")
tata.begin_fill()
tata.forward(2*x/3)
tata.right(90)
tata.forward(x/3)
tata.right(90)
tata.forward(2*x/3)
tata.end_fill()

tata.up()
tata.left(90)
tata.forward(x/4)
tata.left(90)
tata.forward(x/3)
tata.down()

tata.fillcolor("gray")
tata.begin_fill()
for i in range(4):
    tata.forward(x/3)
    tata.right(90)
tata.end_fill()
   
tata.up()
tata.right(90)
tata.forward(x/4)
tata.forward(x/4)
tata.left(90)
tata.down()

tata.fillcolor("gray")
tata.begin_fill()
for i in range(4):
    tata.forward(x/3)
    tata.right(90)
tata.end_fill()
   
tata.up()
tata.left(90)
tata.forward(x/4+x/4)
tata.right(90)
tata.down()

tata.up()
tata.forward(2*x/3)
tata.right(90)
tata.forward(x+x/2)
tata.left(135)
tata.down()

tata.fillcolor("blueviolet")
tata.begin_fill()
tata.forward(x*2)
tata.left(90)
tata.forward(x*2)
tata.left(135)
tata.forward(2*x+x/2+x/3)
tata.end_fill()
turtle.done()