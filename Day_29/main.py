from tkinter import *
from tkinter import messagebox
FONT_NAME = "Courier"
FONT_SIZE = 11
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def valid_inputs(website, email, password):
    if website == "" or email == "" or password == "":
        return False
    return True

def save_password():
    website = input_website.get()
    email_or_usnm = input_username.get()
    password = input_password.get()

    if valid_inputs(website, email_or_usnm, password):
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {email_or_usnm}\n"
                                                      f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website}   |   {email_or_usnm}   |   {password}\n")

            input_password.delete(0, 'end')
            input_website.delete(0, 'end')
    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

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
input_website.focus()

label_username = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
label_username.grid(column=0, row=2)

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2, sticky="EW")
input_username.insert(0, "dominik.test@gmail.pl")

label_password = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
label_password.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3, sticky="EW")

btn_generate_password = Button(text="Generate Password")
btn_generate_password.grid(column=2, row=3, sticky="EW")

btn_add = Button(text="Add", command=save_password)
btn_add.grid(column=1, columnspan=2, row=4, sticky="EW")

window.mainloop()