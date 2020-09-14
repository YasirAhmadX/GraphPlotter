from matplotlib import pyplot
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from math import *

window=Tk()
window.title('GPlot-IV')
window.geometry('300x400')


def PlotEq(X,Y,eq,limity=False):
    global c
    if 'n' in eq or 'c' in eq:
        pyplot.xlabel('X axis (degrees)')
        pyplot.ylabel('Y axis')
        pyplot.title('Graph of '+eq)
    else:
        pyplot.xlabel('X axis')
        pyplot.ylabel('Y axis')
        pyplot.title('Graph of polynomial f(x)='+eq)
    if c!='r':
        pyplot.title('Graph of multiple functions')
    pyplot.plot(X,Y,c,label=eq,linewidth=2)
    #Toggling line color
    if c=='r':
        c='b'
    elif c=='b':
        c='g'
    elif c=='g':
        c='y'
    else:
        c='o'
    #
    if limity:
        pyplot.ylim(-100,100)
    pyplot.legend()
    pyplot.grid(True,color='b')
    pyplot.show()

    #msg.showinfo('Message from Yasir','Kindly close the program! ')

def CordFromEq(eq):
    print('CordFromEq:',eq)
    X=[]
    Y=[]
    x=-1000
    while x<=1000:
        X.append(x)
        Y.append(eval(eq))
        x+=0.1
    if 't' in eq:
        PlotEq(X,Y,eq,limity=True)
    else:
        PlotEq(X,Y,eq)


def Menu():
    def Poly():
        def BTMenu():
            polyframe.destroy()
            Menu()
        def GetDegree():
            def GetEq():
                eq=''
                for i in range(int(deg)+1):
                    eq=eq+' '+c[i].get()+e[i].get()+'* x**'+str(i)
                    if e[i].get()=='':
                        msg.showinfo('Message from EccentriX','Please enter correctt coefficients to their respective polynomials.')
                        Menu()
                    l[i].destroy()
                    c[i].destroy()
                    e[i].destroy()
                polyframe.destroy()
                Menu()
                CordFromEq(eq)

            deg=C0.get()

            L0.destroy()
            BTM.destroy()
            B0.destroy()
            C0.destroy()

            Label(polyframe,text='Enter the equation:').grid(row=2,column=0)
            P0=Button(polyframe,text='Proceed!',command=GetEq)

            l=[]
            e=[]
            c=[]
            for i in range(int(deg)+1):
                l.append(Label(window,text='x^'+str(i)))
                e.append(Entry(window,width=10))
                c.append(Combobox(window,width='2'))
                c[i]['values']=['+','-']
                c[i].current(0)
                c[i].grid(row=3+i,column=0)
                e[i].grid(row=3+i,column=1)
                l[i].grid(row=3+i,column=2)
                if i==int(deg):
                    P0.grid()

        menuframe.destroy()
        polyframe=Frame(window)
        polyframe.grid()

        BTM=Button(polyframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        L0=Label(polyframe,text='Select degree of polynomial: ')

        C0=Combobox(polyframe,width=5)
        C0['values']=[0,1,2,3,4,5,6,7,8,9]
        C0.current(0)

        B0=Button(polyframe,text='Select',command=GetDegree)

        L0.grid(row=2,column=0)
        C0.grid(row=2,column=1)
        B0.grid(row=3,column=1)

    def TrigFun():
        def BTMenu():
            trigframe.destroy()
            Menu()
        def GetCoeff(eqt):
            def GetEq():
                eq=C0.get()
                for i in range(len(eqt)):
                    if eqt[i] in ('x','y'):
                        eq=eq+C1.get()
                    elif eqt[i]=='+':
                        eq=eq+C2.get()
                    elif eqt[i]=='z':
                        eq=eq+C3.get()
                    else:
                        eq=eq+eqt[i]
                print(eq)
                CordFromEq(eq)
            window.geometry('400x400')
            L0.configure(text='Select input for function:'+eqt)
            Label(trigframe,text=' ').grid(row=3,column=0)
            B0.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            if eqt=='sin(y)+cos(z)':
                L1=Label(trigframe,text='sin(')
                L2=Label(trigframe,text=')')
                L3=Label(trigframe,text='cos(')
                L4=Label(trigframe,text=')')
                C0=Combobox(trigframe,width=2)
                C1=Combobox(trigframe,width=5)
                C2=Combobox(trigframe,width=2)
                C3=Combobox(trigframe,width=5)
                C0['values']=['+','-']
                C1['values']=['0.5*x','1*x','1.5*x','2*x']
                C2['values']=['+','-']
                C3['values']=['0.5*x','1*x','1.5*x','2*x']
                C0.current(0)
                C1.current(1)
                C2.current(0)
                C3.current(1)

                C0.grid(row=3,column=1)
                L1.grid(row=3,column=2)
                C1.grid(row=3,column=3)
                L2.grid(row=3,column=4)
                C2.grid(row=3,column=5)
                L3.grid(row=3,column=6)
                C3.grid(row=3,column=7)
                L4.grid(row=3,column=8)

            else:
                L1=Label(trigframe,text=eqt[:-3])
                L2=Label(trigframe,text='))')
                C0=Combobox(trigframe,width=2)
                C0['values']=['+','-']
                C1=Combobox(trigframe,width=5)
                C1['values']=['0.5*x','1*x','1.5*x','2*x']
                C0.current(0)
                C1.current(1)

                C0.grid(row=3,column=1)
                L1.grid(row=3,column=2)
                C1.grid(row=3,column=3)
                L2.grid(row=3,column=4)

            P=Button(trigframe,text='Proceed!',command=GetEq)
            P.grid(row=4,column=2)

        def trigsin():
            eqt='sin(radians(x))'
            GetCoeff(eqt)
        def trigcos():
            eqt='cos(radians(x))'
            GetCoeff(eqt)
        def trigtan():
            eqt='tan(radians(x))'
            GetCoeff(eqt)
        def trigsinNcos():
            eqt='sin(y)+cos(z)'
            GetCoeff(eqt)
        menuframe.destroy()

        trigframe=Frame(window)
        trigframe.grid()

        BTM=Button(trigframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        L0=Label(trigframe,text='Choose type of function:')
        B0=Button(trigframe,text='sin',command=trigsin)
        B1=Button(trigframe,text='cos',command=trigcos)
        B2=Button(trigframe,text='tan',command=trigtan)
        B3=Button(trigframe,text='sin+cos',command=trigsinNcos)

        L0.grid()
        B0.grid()
        B1.grid()
        B2.grid()
        B3.grid()

    def MakeGs():
        def BTMenu():
            mgframe.destroy()
            Menu()
        menuframe.destroy()

        mgframe=Frame(window)
        mgframe.grid()

        BTM=Button(mgframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        Label(mgframe,text='Make Graphs coming soon!').grid()
        Label(mgframe,text='Lookout for GP-V').grid()
    def help():
        def BTMenu():
            helpframe.destroy()
            Menu()
        menuframe.destroy()

        helpframe=Frame(window)
        helpframe.grid()

        BTM=Button(helpframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        Label(helpframe,text='Help coming soon!').grid()

    def AnC():
        def BTMenu():
            ancframe.destroy()
            Menu()
        menuframe.destroy()

        ancframe=Frame(window)
        ancframe.grid()

        BTM=Button(ancframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        Label(ancframe,text='Graph Plotter IV',font=('Times New Roman',20)).grid()
        Label(ancframe,text='\nBy Yasir Ahmad',font=('Arial',8)).grid()
        Label(ancframe,text='\n\nImplementation Project',font=('Times New Roman',15)).grid()
        Label(ancframe,text='\nVisit\nhttps://github.com/YasirAhmad-EccentriX/GraphPlotter\nfor more info regarding future updates and progress.',font=('Times New Roman',15)).grid()

    def exit():
        try:
            pyplot.close()
        except:
            pass
        window.destroy()


    menuframe=Frame(window)
    menuframe.grid(row=0,column=3)

    L0=Label(menuframe,text='Graph Plotter IV\n',font=('Times New Roman',20))
    L1=Label(menuframe,text='MENU',font=('Times New Roman',20))

    B0=(Button(menuframe,text='Plot Polynomal equation',command=Poly,width=30))
    B1=(Button(menuframe,text='Plot T - Functions',command=TrigFun,width=30))
    B2=(Button(menuframe,text='Make Graphs',command=MakeGs,width=30))
    B3=(Button(menuframe,text='Help',command=help,width=30))
    B4=(Button(menuframe,text='About&Credits',command=AnC,width=30))
    B5=(Button(menuframe,text='Exit',command=exit,width=30))


    L0.grid(row=0,column=3)
    L1.grid(row=1,column=3)
    B0.grid(row=2,column=3)
    B1.grid(row=3,column=3)
    B2.grid(row=4,column=3)
    B3.grid(row=5,column=3)
    B4.grid(row=6,column=3)
    B5.grid(row=7,column=3)

c='r' #global line color for toggling

Menu()
window.mainloop()
