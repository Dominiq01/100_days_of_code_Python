from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT_NAME = "Courier"
FONT_SIZE = 11


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    input_password.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in
                                                                        range(randint(2, 4))] + [
                        choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    input_password.insert(0, password)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    user_input = input_website.get().title()

    with open("data.txt") as data_file:
        data = json.load(data_file)
        print(data)

    # messagebox.showinfo(f"{user_input}", message=f"Email: {}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def valid_inputs(website, password):
    if website == "" or password == "":
        return False
    return True


def save_password():
    website = input_website.get()
    email_or_usnm = input_username.get()
    password = input_password.get()
    new_data = {
        website: {
        "email": email_or_usnm,
        "password": password
    }}

    if valid_inputs(website, password):

        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(fp=data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

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
input_website.grid(column=1, row=1, sticky="EW")
input_website.focus()

btn_search_website = Button(text="Search", command=search_website)
btn_search_website.grid(column=2, row=1, sticky="EW")

label_username = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
label_username.grid(column=0, row=2)

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2, sticky="EW")
input_username.insert(0, "dominik.test@gmail.pl")

label_password = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
label_password.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3, sticky="EW")

btn_generate_password = Button(text="Generate Password", command=generate_password)
btn_generate_password.grid(column=2, row=3, sticky="EW")

btn_add = Button(text="Add", command=save_password)
btn_add.grid(column=1, columnspan=2, row=4, sticky="EW")

window.mainloop()
