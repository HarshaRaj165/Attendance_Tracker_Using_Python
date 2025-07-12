import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def mark_attendance():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Warning", "Please enter your name!")
        return

    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')

    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time])

    messagebox.showinfo("Success", f"Attendance marked for {name}")
    name_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("400x200")

tk.Label(root, text="Enter Your Name:", font=("Arial", 14)).pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=5)

tk.Button(root, text="Mark Attendance", font=("Arial", 12), command=mark_attendance, bg="green", fg="white").pack(pady=15)

root.mainloop()
