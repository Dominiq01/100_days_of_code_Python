from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps < 9:
        if reps == 8:
            count_down(round(long_break_sec))
            timer_label.config(text="Break", fg=RED)

        elif reps % 2 == 0:
            count_down(round(short_break_sec))
            timer_label.config(text="Break", fg=PINK)
        else:
            count_down(round(work_sec))
            timer_label.config(text="Work", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    count_convert = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_convert)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        start_timer()
        check_marks = label_check.cget("text")
        if reps % 2 != 0:
            check_marks += "✔"
        label_check.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

button_1 = Button(text="Start", command=start_timer)
button_1.grid(column=0, row=2)

label_check = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

button_2 = Button(text="Reset", command=reset_timer)
button_2.grid(column=2, row=2)

window.mainloop()
