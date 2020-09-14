from math import *
from os import system
from turtle import *

def Verification():
    print('User verification stage\n\t')
    z=input('Enter password: ')
    pwd=['MjnxjsGjwL','Qtsj\tqkd]','Sjr8xnX']
    s=''
    for i in z:
        s=s+(chr(ord(i)+5))
    if s not in pwd:
        input('Invilad password')
        exit()
def MkCplane(a=-650,b=651,n=50,fx=1,fy=1):
    width(1)

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

def MkCGplane(a=-650,b=651,n=50,fx=1,fy=1):
    width(1000)
    goto(700,0)
    goto(-700,0)
    goto(0,0)
    width(1)
    pencolor('green')
    for x in range(a,b,n):
        goto(x,0)
        pd()
        if x==0:
            width(3)
        else:
            width(1)
        sety(-300)
        pu()
        sety(-320)
        pd()
        write(x/fx)
        pu()
        sety(-300)
        pd()
        sety(300)
        pu()
    setx(0)
    for y in range(-300,350,50):
        goto(0,y)
        pd()
        if y==0:
            width(3)
        else:
            width(1)
        setx(a)
        pu()
        setx(a-20)
        pd()
        write(y/fy)
        pu()
        setx(a)
        pd()
        setx(b-(b%n))
        pu()
    sety(0)
    goto(0,0)
def Help():
    print('-'*70,'\n\n')
    print('Credits'.center(70,'-'))
    print('\nProgrammer:- Yasir Ahmad\n')
    print('Purose:- Implementation Practices\n','-'*70,'\n\n')
    print('Help\n')
    print('\tGraphs:-')
    print('\t\tThis program supports 2 types of graph style, i.e. \n\t\t1 Simplified Axis >>>(Only x and y axis are visibal)')
    print('\t\t2 Axis and Grids >>>(Full grid is visibal)')
    print('\n\tMenu(Available Graphing Tools)')
    print('\tThere are 3 types of tools which can be used for graphing')
    print('\n\t\t1 Graph of straight line:-\n\t\t\tUser is expected to enter coefficients of variables in General Equation Form of straight line viz. Ax+By+C=0')
    print('\n\t\t2 Graph of polynomial functions;-\n\t\t\tUser needs to enter degree of polynomial and then enter coresponding coefficients')
    print('\n\t\t3 Graph of T-functions(Trignometric functions)\n\t\t\tThere are 3 T-functions available(sin,cos,tan) and user can choose any 1')
    print('\t\t\tGraph is ploted taking x cordinates as degrees(*not radians) and is upscaled (x200) on y-axis')
    print('\t\t\tCoefficient of angle:-If user enters 2 and had chosen sin function then program will graph sin(2x).\n\t\t\tSimilary if 0.5 is enterend and cos has been chosen then program will graph cos(x/2)')
    print('\n\tExit:-\n\t\t\tIt just exits the program!')
    print('-'*70,'\n\n')
def G_Style(a=-650,b=651,n=50,fx=1,fy=1):
    speed(0)
    hideturtle()
    if gstyle=='1':
        MkCplane(a,b,n,fx,fy)
    elif gstyle=='2':
        MkCGplane(a,b,n,fx,fy)
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
    G_Style()
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
    fx=float(input('Enter the coefficient of angle (Refer to help): '))
    print('Graph has been scaled (x 200px) on y-axis')
    n=input('Enter integer resolution(accuracy) of graph[lower value,longer time]: ')
    G_Style(-660,661,fy=200,n=30)
    pu()
    goto(-660,f(-660*pi/180)*200)
    pd()
    pencolor('blue')
    speed(0)
    width(2)
    for x in range(-660,661,int(n)):
        y=f(fx*x*pi/180)*200
        goto(x,y)
        if y==0:
            pencolor('red');width(1)
            goto(x,y+20)
            write('X_intercept='+str(x/200));pu()
            goto(x,y-20);pd()
            goto(x,y)
            pencolor('blue');width(2)
        if x==0:
            pencolor('red');width(1)
            goto(x+20,y)
            write('Y_intercept='+str(y/200));pu()
            goto(x-20,y);pd()
            goto(x,y)
            pencolor('blue');width(2)

def Menu():

    z=input('Menu\n\n\tEnter 1 to plot graph of a straight line\n\n\tEnter 2 to plot polynomial equation\n\n\tEnter 3 to plot T-functions\n\n\tEnter 4 for help\n\n\tEnter 5 to quit\n')
    if z=='1':
        try:
            A=float(input('\nEnter coefficient of x: '))
            B=float(input('Enter coefficient of y: '))
            C=float(input('Enter constant term: '))
            SLanalysis(A,B,C)
            G_Style()
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
        Help()
        Menu()
    elif z=='5':
        exit()
    else:
        input('invalid input')
        Menu()
    print('Click on the graph to clear it!')
    Screen().exitonclick()
    Menu()
system('title Verify for GraphPlotter  by  YSR')
Verification()
system('cls')
system('title GraphPlotter  by  YSR')
system('color 0A')
gstyle=input('Select Graph style:\n\t1\tSimplified Axis\n\t2\tAxis and Grids\n')
Menu()
