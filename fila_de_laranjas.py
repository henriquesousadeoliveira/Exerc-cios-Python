import turtle
import math

tata=turtle.Turtle()

razao=30
for raio in range(20,200,razao):
    tata.fillcolor("orange")
    tata.begin_fill()
    tata.circle(raio)
    tata.up()
    distancia = math.sqrt( (2*raio+razao)**2 - razao**2 )
    tata.fd(distancia)
    tata.down()
    tata.end_fill()
    
tata.done()
    
