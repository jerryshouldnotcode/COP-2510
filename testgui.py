import tkinter as tk

window = tk.Tk()
window.title('TestGUI')

windowLabel = tk.Label(window, text = 'Python Rocks!')
windowLabel.pack(side = 'top', ipadx= 75, ipady = 75)

#button time!
windowButton1 = tk.Button(window, text = 'Agreed!', borderwidth = 4, relief = 'raised')
windowButton2 = tk.Button(window, text = 'Meh.', borderwidth = 4, relief = 'raised')

windowButton1.pack(side = 'left', ipadx = 30, ipady = 30)
windowButton2.pack(side = 'right', ipadx = 30, ipady = 30)


#space for entry? Uh, yeah?!
windowEntry = tk.Entry(window, borderwidth = 2, relief = 'solid')
windowEntry.pack(side = 'top', ipadx = 20, ipady = 20)



window.mainloop()
