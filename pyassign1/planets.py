
# coding: utf-8

# In[ ]:


import math
pi=math.pi

def function(degree,e,a,b):
    x=a*math.cos(degree)
    y=b*math.sin(degree)
    u=x*math.cos(e)+y*math.sin(e)
    v=x*math.sin(e)-y*math.cos(e)
    return u,v

def main():
    import turtle
    sun=turtle.Turtle()
    mercury=turtle.Turtle()
    venus=turtle.Turtle()
    earth=turtle.Turtle()
    mars=turtle.Turtle()
    jupiter=turtle.Turtle()
    saturn=turtle.Turtle()
    colors=['yellow','blue','green','red','brown','orange','sea green']
    planets=['sun','mercury','venus','earth','mars','jupiter','saturn']
    initial=[0,50,60,100,130,160,170]
    sun.color(colors[0])
    mercury.color(colors[1])
    venus.color(colors[2])
    earth.color(colors[3])
    mars.color(colors[4])
    jupiter.color(colors[5])
    saturn.color(colors[6])
    
    sun.shape("circle")
    sun.penup()
    mercury.shape("circle")
    mercury.penup()
    venus.shape("circle")
    venus.penup()
    earth.shape("circle")
    earth.penup()
    mars.shape("circle")
    mars.penup()
    jupiter.shape("circle")
    jupiter.penup()
    saturn.shape("circle")
    saturn.penup()
    
    sun.forward(initial[0])
    mercury.forward(initial[1])
    venus.forward(initial[2])
    earth.forward(initial[3])
    mars.forward(initial[4])
    jupiter.forward(initial[5])
    saturn.forward(initial[6])
        
    sun.left(90)
    sun.down()
    mercury.left(90)
    mercury.down()
    venus.left(90)
    venus.down()
    earth.left(90)
    earth.down()
    mars.left(90)
    mars.down()
    jupiter.left(90)
    jupiter.down()
    saturn.left(90)
    saturn.down()
    
    for i in range(1000):
        mercury.forward(100*pi/180)
        mercury.left(1)
        venus.goto(function(pi*i/180,pi/18,60,55))
        earth.goto(function(pi*i/180,0,100,80))
        mars.goto(function(pi*i/180,pi/10,130,60))
        jupiter.goto(function(pi*i/180,0,160,40))
        saturn.goto(function(pi*i/180,-pi/10,170,90))
    
if __name__ == '__main__':
    main()

