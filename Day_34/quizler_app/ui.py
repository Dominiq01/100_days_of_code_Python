from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, columnspan=2, column=0)
        self.canvas.create_text(150, 125, text="TEST TEST", font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")
        self.button_true = Button(image=self.img_true)
        self.button_true.grid(column=0, row=2)
        self.button_false = Button(image=self.img_false)
        self.button_false.grid(column=1, row=2)

        self.window.mainloop()
