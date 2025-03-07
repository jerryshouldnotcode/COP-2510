#intro to GUI - Graphical User Interfaces
# a window that allows users to interact with features available in an application
#the tkinter module - tk interface

#windows, frames, buttons, entry box, button with message box

#assignment: make a little username submission thing

#
import tkinter

#class definition
class FirstGUI:
    def __init__(self):
        #creating a window
        self.mainwindow = tkinter.Tk() #creating an instance

        #create a title for the window
        self.mainwindow.title('My first GUI Window')

        #display text with labels
        #relief styles = groove, sunken, ridge, flat, raised, solid
        #self.label = tkinter.Label(self.mainwindow, text = 'My first label in a GUI', borderwidth = 4, relief = 'raised')

        #use pack method to specify where in the window the label should go
        #self.label.pack(side = 'bottom') #options: bottom, left, right, top
        
        #create frames to segment the window
        self.top = tkinter.Frame(self.mainwindow, borderwidth = 5, relief = 'raised')
        self.bottom = tkinter.Frame(self.mainwindow, borderwidth = 7, relief = 'groove')

        #create labels for each frame
        self.toplabel = tkinter.Label(self.top, text = 'Top Frame Label', borderwidth = 3, relief = 'solid')
        self.bottomlabel = tkinter.Label(self.bottom, text = 'Bottom Frame Label', borderwidth = 4, relief = 'flat')

        #use pack method for each frame
        self.top.pack(side = 'top', ipadx = 75, ipady = 75)
        self.bottom.pack(side = 'top', ipadx = 75, ipady = 75)

        #use pack method for each label
        self.toplabel.pack(side = 'bottom', ipadx = 75, ipady = 75)
        self.bottomlabel.pack(side = 'top', ipadx = 75, ipady = 75)

        #create a button
        self.button = tkinter.Button(self.mainwindow, relief = 'raised')
        self.buttonLabel = tkinter.Label(self.button, text = 'Click me')
        self.button.pack(side = 'bottom', ipadx = 30, ipady = 30)
        self.buttonLabel.pack(side = 'bottom')
        
        
                                


            
        #enter the tkinter main loop
        tkinter.mainloop()  #keeps the interface running

        
#driver portion

#create an object
my1stgui = FirstGUI()
my1st
