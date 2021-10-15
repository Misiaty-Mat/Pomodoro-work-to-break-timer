from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Reset program
def reset_timer():
    window.after_cancel(timer)
    main_banner.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")

    global reps
    reps = 0


# Starts timer and show if it is brake or work time
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        cout_down(LONG_BREAK_MIN * 60)
        main_banner.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        cout_down(SHORT_BREAK_MIN * 60)
        main_banner.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        cout_down(WORK_MIN * 60)
        main_banner.config(text="Work", fg=GREEN)


# Countdown mechanics
def cout_down(count: int):
    minutes = count // 60
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    # showing time on canvas
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, cout_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2

        # checkmarks control
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# window setup
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Main banner setup
main_banner = Label(text="Timer", font=(FONT_NAME, 30), bg=YELLOW)
main_banner.grid(column=1, row=0)
main_banner.config(fg=GREEN)

# Canvas with image and timer setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button setup
start_btn = Button(text="Start", width=10, fg=RED, font=(FONT_NAME, 18),
                   highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

# Reset button setup
reset_btn = Button(text="Reset", width=10, fg=RED, font=(FONT_NAME, 18),
                   highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Checkmarks label setup
checkmarks = Label(font=(FONT_NAME, 30), bg=YELLOW)
checkmarks.grid(column=1, row=3)
checkmarks.config(fg=GREEN)


window.mainloop()
