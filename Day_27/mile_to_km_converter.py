from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=100)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

converted_label = Label(text=0)
converted_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def convert_miles_to_km():
    input_val = float(user_input.get())
    output = input_val * 1.60934
    converted_label.config(text=str(round(output,2)))

calc_button = Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()