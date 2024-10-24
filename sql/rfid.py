import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to connect to the database
def connect_db():
    return sqlite3.connect('local_attendance.db')

# Function to process the scanned RFID tag
def process_rfid(event=None):
    rfid_tag = rfid_entry.get()
    if rfid_tag:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM attendance WHERE rfid_tag = ?', (rfid_tag,))
        record = cursor.fetchone()
        conn.close()
        
        if record:
            details = f"ID: {record[0]}\nName: {record[1]}\nRFID Tag: {record[2]}\nDate: {record[3]}\nTime: {record[4]}\nReason: {record[5]}"
            messagebox.showinfo("RFID Details", details)
        else:
            messagebox.showwarning("Not Found", "No record found for this RFID tag.")
        rfid_entry.delete(0, tk.END)  # Clear entry after processing
    else:
        messagebox.showwarning("Input Error", "Please scan an RFID tag.")

# Function to start scanning RFID
def scan_rfid_usb():
    # Clear the entry and set focus
    rfid_entry.delete(0, tk.END)
    rfid_entry.focus_set()
    messagebox.showinfo("Scan RFID", "Please scan the RFID tag...")

# Function to book an appointment
def book_appointment():
    name = simpledialog.askstring("Book Appointment", "Enter Name:")
    rfid_tag = simpledialog.askstring("Book Appointment", "Enter RFID Tag:")
    date = simpledialog.askstring("Book Appointment", "Enter Date (YYYY-MM-DD):")
    time = simpledialog.askstring("Book Appointment", "Enter Time (HH:MM:SS):")
    reason = simpledialog.askstring("Book Appointment", "Enter Reason:")
    
    if all([name, rfid_tag, date, time, reason]):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO attendance (name, rfid_tag, date, time, reason) VALUES (?, ?, ?, ?, ?)''',
                       (name, rfid_tag, date, time, reason))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment booked successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields must be filled.")

# Function to view all records
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
root.title("RFID Attendance System")
root.geometry("400x300")

# Creating an entry for RFID scanning
rfid_entry = tk.Entry(root, font=('Helvetica', 12), width=30)
rfid_entry.pack(pady=20)

# Binding the Return key to process the scanned RFID
rfid_entry.bind("<Return>", process_rfid)

# Creating buttons for the options
scan_usb_button = tk.Button(root, text="Scan RFID from USB", command=scan_rfid_usb)
scan_usb_button.pack(pady=10)

book_button = tk.Button(root, text="Book Appointment", command=book_appointment)
book_button.pack(pady=10)

view_button = tk.Button(root, text="View Records", command=view_records)
view_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
