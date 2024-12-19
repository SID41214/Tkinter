import tkinter

window = tkinter.Tk()
window.title("Layout and Grid")

# Creating 2 text labels and input labels

tkinter.Label(window,text="Username").grid(row=0) #this is places in 0 0

# 'Entry'is used to display the input fields
tkinter.Entry(window).grid(row=0,column=1) #    this is places in 0  1

# here password only for explaining the grid not for the as hidden field
tkinter.Label(window,text="Password").grid(row=1) # this is places in  1  0 
tkinter.Entry(window).grid(row=1,column=1) # this is places in 1  1

# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window,text="Keep Me logged in").grid(columnspan=2) #'Columnspan' tells to take the width of 2 columns 

# you can also use 'rowspan' in the similar manner

window.mainloop() 
 
