from math import *
from os import system
from turtle import *
system('title GraphPlotter  by  YSR')
system('color 0A')
def MkCplane(a=-650,b=700,n=50):
    width(1)
    speed(0)
    pencolor('black')
    for x in range(a,b,n):
        goto(x,0)
        if x==0:
            continue
        sety(3)
        write(x)
        sety(0)
    setx(0)
    for y in range(-300,350,50):
        goto(0,y)
        if y==0:
            setx(-10)
        else:
            setx(-25)
        write(y)
        setx(0)
    sety(0)
    goto(0,0)
def SLplot(A,B,C):
    pu()
    goto(-650,(-A/B)*(-650) - C/B)
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-650,651):
        y= (-A/B)*x - C/B
        goto(x,y)
        if y==0:
            pencolor('red');width(1)
            goto(x,y+20)
            write('X_intercept='+str(x));pu()
            goto(x,y-20);pd()
            goto(x,y)
            pencolor('blue');width(2)
        if x==0:
            pencolor('red');width(1)
            goto(x+20,y)
            write('Y_intercept='+str(y));pu()
            goto(x-20,y);pd()
            goto(x,y)
            pencolor('blue');width(2)
def SLanalysis(A,B,C):
    itrcptX=-C/B
    itrcptY=-C/A
    m=-A/B
    print('\n\n\t\t\t--Line-Analysis--')
    print('Y intercept =',itrcptX,'\nX intercept =',itrcptY,'\nSlope =',m,end='\n\n')
def Quadratic(A,B,C):
    pu()
    goto(-650,(A*422500 - B*650 + C))
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-650,651,5):
        y= A*(x**2) + B*x + C
        goto(x,y)
        if y==0:
            pencolor('red');width(1)
            goto(x,y+20)
            write(x)
            goto(x,y-20)
            goto(x,y)
            pencolor('blue');width(2)
        if x==0:
            pencolor('red');width(1)
            goto(x+20,y)
            write(y)
            goto(x-20,y)
            goto(x,y)
            pencolor('blue');width(2)

def trigFn(f):
    print('Graph has been scaled(x100) in y-axis')
    n=input('Enter integer resolution(accuracy) of graph[lower value,longer time]: ')
    MkCplane(-660,661,30)
    pu()
    goto(-660,f(-660*pi/180))
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-660,661,int(n)):
        goto(x,f(x*pi/180)*100)
        
def Menu():
    z=input('Enter 1 to plot graph of a straight line\nEnter 2 to plot quadratic equation\nEnter 3 to plot trig functions\nEnter 4 to quit\n')
    if z=='1':
        try:
            A=float(input('\nEnter coefficient of x: '))
            B=float(input('Enter coefficient of y: '))
            C=float(input('Enter constant term: '))
            SLanalysis(A,B,C)
            MkCplane()
            SLplot(A,B,C)
    
        except:
            print('unknown error\nContact programmer')
    elif z=='2':
        try:
            A=float(input('\nEnter coefficient of x^2: '))
            B=float(input('Enter coefficient of x: '))
            C=float(input('Enter constant term: '))
            MkCplane()
            Quadratic(A,B,C)
    
        except:
            print('unknown error\nContact programmer')
    elif z=='3':
        f=input('\nEnter serial no. of desired function\n\n1  sin\n2  cos\n3  tan\n\n')
        if f=='1':
            f=sin
        elif f=='2':
            f=cos
        elif f=='3':
            print('Remember computers are not good at representing infinity')
            print('So graph of tan might glicth when tan(x) tends to infinity')
            f=tan
        else:
            input('invalid input')
            Menu()
        trigFn(f)
    elif z=='4':
        exit()
    else:
        input('invalid input')
        exit()
    Screen().exitonclick()
Menu()    
        
            
