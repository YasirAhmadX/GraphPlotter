from math import *
from os import system
from turtle import *
system('title GraphPlotter  by  YSR')
system('color 0A')
def MkCplane(a=-650,b=700,n=50,fx=1,fy=1):
    width(1)
    speed(0)
    pencolor('black')
    for x in range(a,b,n):
        goto(x,0)
        if x==0:
            continue
        sety(3)
        write(x/fx)
        sety(0)
    setx(0)
    for y in range(-300,350,50):
        goto(0,y)
        if y==0:
            setx(-10)
        else:
            setx(-25)
        write(y/fy)
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

def poly(z,n):
    l=[]
    for i in range(z+1):
        print('Enter the coefficient of x^',i,' :',sep='',end=' ')
        l.append(int(input()))
    MkCplane()
    pu()
    goto(-700,0)
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-700,701,n):
        y=0
        for i in range(len(l)):
            y+=l[i]*(x**i)
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

def trigFn(f):
    n=input('Enter integer resolution(accuracy) of graph[lower value,longer time]: ')
    MkCplane(-660,661,fy=200,n=30)
    pu()
    goto(-660,f(-660*pi/180)*200)
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-660,661,int(n)):
        y=f(x*pi/180)*200
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
        
def Menu():
    z=input('Enter 1 to plot graph of a straight line\nEnter 2 to plot polynomial equation\nEnter 3 to plot trig functions\nEnter 4 to quit\n')
    if z=='1':
        try:
            A=float(input('\nEnter coefficient of x: '))
            B=float(input('Enter coefficient of y: '))
            C=float(input('Enter constant term: '))
            SLanalysis(A,B,C)
            MkCplane()
            SLplot(A,B,C)
    
        except:
            print('Unknown error\nContact programmer')
    elif z=='2':
        try:
            z=int(input('Enter degree of the polynomial: '))
            n=int(input('Enter integer resolution(accuracy) of graph[lower value,longer time](min res=1px): '))
            poly(z,n)
        except :
            print('Error!\tFunction might be undefined at some point\nContact programmer')
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
        
            
