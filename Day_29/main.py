from tkinter import *
FONT_NAME = "Courier"
FONT_SIZE = 11
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
label_website.grid(column=0, row=1)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")

label_username = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
label_username.grid(column=0, row=2)

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
label_password.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3, sticky="EW")

btn_generate_password = Button(text="Generate Password")
btn_generate_password.grid(column=2, row=3, sticky="EW")

btn_add = Button(text="Add")
btn_add.grid(column=1, columnspan=2, row=4, sticky="EW")

window.mainloop()