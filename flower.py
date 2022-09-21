from turtle import *
def flower (c,start,stop,step,f) :
    color(c)
    for i in range(10):
        for j in range(start,stop,step):
            pensize(j)
            forward(f)
        penup()
        goto(0,0)
        pendown()
        left(36)


bgcolor("lightgreen")
flower("red",20,60,2,5)
flower("orange", 10,30,1,3)
flower("black",0,15,1,2)
    
pensize(20)
color("olive")   
goto(0,0)

