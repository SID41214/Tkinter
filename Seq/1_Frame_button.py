# 1.Giving frame and buttons 
import tkinter

window = tkinter.Tk()
window.title("This's Our Title")

# Set window size(width x height)
window.geometry("400x300") 

# Creating 2 frames TOP and BOTTOM 

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack()

# Now, create some widgets in the top_frame and bottom_frame

btn1=tkinter.Button(top_frame,text="Button 1",fg='red').pack()
btn2=tkinter.Button(top_frame,text="Button 2",fg='green').pack()
btn3=tkinter.Button(top_frame,text="Button 3",fg='purple').pack(side='left')
btn4=tkinter.Button(top_frame,text="Button 4",fg='orange').pack(side='left')

window.mainloop()