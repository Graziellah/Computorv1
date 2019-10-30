import Equation
from tkinter import *
import sys

class MyApp():
    def __init__(self): 
        self.window = Tk()
        self.window.title('ComputerV1')
        self.window.geometry("1000x700")
        self.window.minsize(480, 360)
        frame = Frame(self.window, bg='#048B9A')
        self.window.config(background='#048B9A')
        title_label = Label(frame,text='Polynomial equation solver', font=('Courier', 30), bg='#048B9A', fg='white')
        title_label.pack(pady=30)
        self.yt_input = Entry(frame, font=('Courier', 30), fg='#048B9A', bg='white', width='30')
        self.yt_input.pack(pady=30)
        yt_button = Button(frame,text='Calculate', font=('Courier', 30), fg='#048B9A', bg='white', command=self.display)
        yt_button.pack(pady=10)
        self.Texte = StringVar()
        display_label = Label(frame,textvariable = self.Texte, font=('Courier', 30), bg='#048B9A', fg='white')
        display_label.pack()
        frame.pack(pady=30)

    def display(self):
        equa = self.yt_input.get()
        result = Equation.Equation(equa)
        try:
            result.split()
            result.calculateDegreValue()
        except (SyntaxError, ValueError) as err:
            self.Texte.set(err)
        except KeyboardInterrupt:
            sys.exit(1)
        else:
            result.solve()
            self.Texte.set(result.displaySoluce())


try:
    app = MyApp()
    app.window.mainloop()
except:
    sys.exit(1)
