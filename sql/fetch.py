import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to connect to the database
def connect_db():
    return sqlite3.connect('local_attendance.db')

# Function to view all records from the attendance table
def view_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM attendance')
    
    records = cursor.fetchall()
    conn.close()

    if records:
        details = "\n".join([f"ID: {record[0]}, Name: {record[1]}, RFID Tag: {record[2]}, Date: {record[3]}, Time: {record[4]}, Reason: {record[5]}" for record in records])
        messagebox.showinfo("Attendance Records", details)
    else:
        messagebox.showinfo("Attendance Records", "No records found.")

# Setting up the main window
root = tk.Tk()
root.title("View Attendance Records")

# Creating a button to view records
view_button = tk.Button(root, text="View Records", command=view_records)
view_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
