import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#357C3C"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = 10
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        count_down(long_break)
        title_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:

        count_down(short_break)
        title_label.config(text="Short Break", fg=PINK)

    else:

        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math


def count_down(count):
    global timer
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif 1 <= count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 37, "bold"))
title_label.grid(column=1, row=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = tkinter.Button(text="Start", fg="white", bg=RED, font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", fg="white", bg=RED, font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)

canvas.grid(column=1, row=1)
window.mainloop()
