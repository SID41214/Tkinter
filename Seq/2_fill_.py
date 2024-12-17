import tkinter

window = tkinter.Tk()
window.title("Here we go again (pack-side-fill-width-height) ")

# Set window size(width x height)
window.geometry("400x300") 

# Creating 3 simple Labels containing any 

# Sufficient Width
tkinter.Label(window, text='Sufficient Width',fg='white',bg='purple').pack()

# width of x
tkinter.Label(window, text='Taking all available width of x',fg='white',bg='green').pack(fill='x')

# height of y
tkinter.Label(window, text='Taking all available width of y',fg='white',bg='black').pack(side='left',fill='y')

window.mainloop()
