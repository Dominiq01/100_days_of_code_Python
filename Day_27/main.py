from tkinter import *

window = Tk()
window.title("TEST")

window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Labels

my_label = Label(text="My Label", font=("Arial", 24, "bold"))

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=4, row=3)

# Buttons
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=2, row=2)

button2 = Button(text="Click me 2", command=button_clicked)
# button.pack()
button2.grid(column=3, row=0)

window.mainloop()