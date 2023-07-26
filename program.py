import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

label = tk.Label(root, font=("Helvetica", 48), fg="white", bg="black")
label.pack(expand=True)

update_time()
root.mainloop()
