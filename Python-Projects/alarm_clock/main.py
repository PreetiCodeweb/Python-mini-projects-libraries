from tkinter import *
from tkinter import ttk
import datetime
import winsound

root = Tk()
root.title("Modern Alarm Clock")
root.geometry("450x300")
root.resizable(False, False)

alarm_time = None
alarm_triggered = False

title = Label(
    root,
    text="⏰ Alarm Clock",
    font=("Segoe UI", 22, "bold")
)
title.pack(pady=10)

clock_label = Label(
    root,
    text="00:00:00",
    font=("Consolas", 28, "bold")
)
clock_label.pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

hour_var = StringVar(value="00")
hours = [f"{i:02d}" for i in range(24)]

ttk.Combobox(
    frame,
    textvariable=hour_var,
    values=hours,
    width=5,
    state="readonly"
).grid(row=0, column=0, padx=5)

minute_var = StringVar(value="00")
minutes = [f"{i:02d}" for i in range(60)]

ttk.Combobox(
    frame,
    textvariable=minute_var,
    values=minutes,
    width=5,
    state="readonly"
).grid(row=0, column=1, padx=5)

second_var = StringVar(value="00")

ttk.Combobox(
    frame,
    textvariable=second_var,
    values=minutes,
    width=5,
    state="readonly"
).grid(row=0, column=2, padx=5)

status_label = Label(
    root,
    text="No Alarm Set",
    font=("Segoe UI", 12)
)
status_label.pack(pady=10)

def set_alarm():
    global alarm_time, alarm_triggered

    alarm_time = (
        f"{hour_var.get()}:"
        f"{minute_var.get()}:"
        f"{second_var.get()}"
    )

    alarm_triggered = False

    status_label.config(
        text=f"Alarm set for {alarm_time}"
    )

def ring_alarm():
    status_label.config(
        text="🔔 Wake Up!",
        fg="red"
    )
    winsound.PlaySound(
        "alarm.wav",
        winsound.SND_ASYNC
    )

    root.bell()

def update_clock():
    global alarm_triggered

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    clock_label.config(text=current_time)

    if (
        alarm_time is not None
        and current_time == alarm_time
        and not alarm_triggered
    ):
        alarm_triggered = True
        ring_alarm()

    root.after(1000, update_clock)

Button(
    root,
    text="Set Alarm",
    font=("Segoe UI", 12, "bold"),
    command=set_alarm
).pack(pady=10)

update_clock()

root.mainloop()