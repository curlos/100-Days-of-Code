from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_pomo = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer_pomo)
    reps = 0
    timer_label.config(text="Timer")
    checkmarks_label.config(text="")
    canvas.itemconfig(
        timer_text, text=f"00:00")

    start_button.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    start_button.config(state=DISABLED)

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0 and reps < 8:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        checkmarks_label.config(text=f"{'✓' * (reps // 2)}")
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        checkmarks_label.config(text=f"{'✓' * (reps // 2)}")
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    canvas.itemconfig(
        timer_text, text=f"{str(count_min).rjust(2, '0')}:{str(count_sec).rjust(2, '0')}")

    if count > 0:
        global timer_pomo
        timer_pomo = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(fg=GREEN, font=(
    FONT_NAME, 35), bg=YELLOW, highlightthickness=0)
checkmarks_label.grid(column=1, row=3)


window.mainloop()
