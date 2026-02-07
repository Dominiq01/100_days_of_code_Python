from tkinter import *

from Day_34.quizler_app.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, columnspan=2, column=0, pady=30)
        self.curr_question_text = self.canvas.create_text(150, 125, text="TEST TEST", font=("Arial", 16, "italic"),
                                                          fill=THEME_COLOR, width=260)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 18, "bold"))
        self.score_label.grid(row=0, column=1)

        self.img_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.img_true, highlightthickness=0, command=lambda: self.give_answer("true"))
        self.button_true.grid(column=0, row=2)

        self.img_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.img_false, highlightthickness=0, command=lambda: self.give_answer("false"))
        self.button_false.grid(column=1, row=2)

        self.button_reset = Button(text="Retry", command=self.reset_quiz)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.canvas.itemconfig(self.curr_question_text, fill=THEME_COLOR)
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.curr_question_text, text=question_text)

    def give_answer(self, answer: str):
        correct_answer = self.quiz.check_answer(answer)
        self.canvas.itemconfig(self.curr_question_text, fill="white")
        if correct_answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.curr_question_text, fill=THEME_COLOR)
            self.score_label.grid_remove()
            self.canvas.itemconfig(self.curr_question_text, text=f"Your final score is: "
                                                                 f"{self.quiz.score}/{self.quiz.question_number}")
            self.button_true.grid_remove()
            self.button_false.grid_remove()
            self.button_reset.grid(column=0, row=2, columnspan=2)

    def reset_quiz(self):
        self.button_reset.grid_remove()
        self.window.quit()
        self.window.destroy()
        new_quiz = QuizBrain()
        self.__init__(new_quiz)

