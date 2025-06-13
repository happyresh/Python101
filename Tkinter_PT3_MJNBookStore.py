# Contributors: Gatchalian, Recio, Latoy, Urbano
# Date: June 01, 2025
# Integrative Programming - Tkinter Programming Task #3

from tkinter import *
from tkinter import ttk, messagebox

def toggle_check1():
    if check1_var.get() == 1:
        combo1.config(state="readonly")
        qty1.config(state="normal")
    else:
        combo1.set("")
        combo1.config(state="disabled")
        price1.config(state="normal")
        price1.delete(0, END)
        price1.config(state="disabled")
        qty1.delete(0, END)
        qty1.config(state="disabled")
        sub1.config(state="normal")
        sub1.delete(0, END)
        sub1.config(state="readonly")

def toggle_check2():
    if check2_var.get() == 1:
        combo2.config(state="readonly")
        qty2.config(state="normal")
    else:
        combo2.set("")
        combo2.config(state="disabled")
        price2.config(state="normal")
        price2.delete(0, END)
        price2.config(state="disabled")
        qty2.delete(0, END)
        qty2.config(state="disabled")
        sub2.config(state="normal")
        sub2.delete(0, END)
        sub2.config(state="readonly")

def toggle_check3():
    if check3_var.get() == 1:
        combo3.config(state="readonly")
        qty3.config(state="normal")
    else:
        combo3.set("")
        combo3.config(state="disabled")
        price3.config(state="normal")
        price3.delete(0, END)
        price3.config(state="disabled")
        qty3.delete(0, END)
        qty3.config(state="disabled")
        sub3.config(state="normal")
        sub3.delete(0, END)
        sub3.config(state="readonly")

def update_price1(event):
    level = combo1.get()
    price1.config(state="normal")
    price1.delete(0, END)
    if level == "NURSERY":
        price1.insert(0, "150")
    elif level == "KINDER":
        price1.insert(0, "200")
    elif level == "PREP":
        price1.insert(0, "250")
    price1.config(state="disabled")

def update_price2(event):
    level = combo2.get()
    price2.config(state="normal")
    price2.delete(0, END)
    if level == "NURSERY":
        price2.insert(0, "150")
    elif level == "KINDER":
        price2.insert(0, "200")
    elif level == "PREP":
        price2.insert(0, "250")
    price2.config(state="disabled")

def update_price3(event):
    level = combo3.get()
    price3.config(state="normal")
    price3.delete(0, END)
    if level == "NURSERY":
        price3.insert(0, "150")
    elif level == "KINDER":
        price3.insert(0, "200")
    elif level == "PREP":
        price3.insert(0, "250")
    price3.config(state="disabled")

def compute_total():
    total = 0
    try:
        if check1_var.get() == 1:
            p = float(price1.get())
            q = int(qty1.get())
            subtotal = p * q
            sub1.config(state="normal")
            sub1.delete(0, END)
            sub1.insert(0, f"{subtotal:.2f}")
            sub1.config(state="readonly")
            total += subtotal
        if check2_var.get() == 1:
            p = float(price2.get())
            q = int(qty2.get())
            subtotal = p * q
            sub2.config(state="normal")
            sub2.delete(0, END)
            sub2.insert(0, f"{subtotal:.2f}")
            sub2.config(state="readonly")
            total += subtotal
        if check3_var.get() == 1:
            p = float(price3.get())
            q = int(qty3.get())
            subtotal = p * q
            sub3.config(state="normal")
            sub3.delete(0, END)
            sub3.insert(0, f"{subtotal:.2f}")
            sub3.config(state="readonly")
            total += subtotal
        total_entry.config(state="normal")
        total_entry.delete(0, END)
        total_entry.insert(0, f"{total:.2f}")
        total_entry.config(state="readonly")
    except:
        messagebox.showerror("Error", "Please enter valid quantity.")

def clear_all():
    for cb, combo, price, qty, sub in [
        (check1_var, combo1, price1, qty1, sub1),
        (check2_var, combo2, price2, qty2, sub2),
        (check3_var, combo3, price3, qty3, sub3)
    ]:
        cb.set(0)
        combo.set("")
        combo.config(state="disabled")
        price.config(state="normal")
        price.delete(0, END)
        price.config(state="disabled")
        qty.delete(0, END)
        qty.config(state="disabled")
        sub.config(state="normal")
        sub.delete(0, END)
        sub.config(state="readonly")
    total_entry.config(state="normal")
    total_entry.delete(0, END)
    total_entry.config(state="readonly")

# --- GUI Layout ---
frame = Tk()
frame.title("MJN Book Store")

Label(frame, text="Book Title").grid(row=0, column=0)
Label(frame, text="Level").grid(row=0, column=1)
Label(frame, text="Unit Price").grid(row=0, column=2)
Label(frame, text="Quantity").grid(row=0, column=3)
Label(frame, text="Sub-Total").grid(row=0, column=4)

# Row 1
check1_var = IntVar()
Checkbutton(frame, text="Everyday English", variable=check1_var, command=toggle_check1).grid(row=1, column=0, sticky='w')
combo1 = ttk.Combobox(frame, values=["", "NURSERY", "KINDER", "PREP"], state="disabled", width=10)
combo1.grid(row=1, column=1)
combo1.bind("<<ComboboxSelected>>", update_price1)
price1 = Entry(frame, state="disabled", width=10)
price1.grid(row=1, column=2)
qty1 = Entry(frame, state="disabled", width=10)
qty1.grid(row=1, column=3)
sub1 = Entry(frame, state="readonly", width=10)
sub1.grid(row=1, column=4)

# Row 2
check2_var = IntVar()
Checkbutton(frame, text="Integrated Mathematics", variable=check2_var, command=toggle_check2).grid(row=2, column=0, sticky='w')
combo2 = ttk.Combobox(frame, values=["", "NURSERY", "KINDER", "PREP"], state="disabled", width=10)
combo2.grid(row=2, column=1)
combo2.bind("<<ComboboxSelected>>", update_price2)
price2 = Entry(frame, state="disabled", width=10)
price2.grid(row=2, column=2)
qty2 = Entry(frame, state="disabled", width=10)
qty2.grid(row=2, column=3)
sub2 = Entry(frame, state="readonly", width=10)
sub2.grid(row=2, column=4)

# Row 3
check3_var = IntVar()
Checkbutton(frame, text="Wonders of Science", variable=check3_var, command=toggle_check3).grid(row=3, column=0, sticky='w')
combo3 = ttk.Combobox(frame, values=["", "NURSERY", "KINDER", "PREP"], state="disabled", width=10)
combo3.grid(row=3, column=1)
combo3.bind("<<ComboboxSelected>>", update_price3)
price3 = Entry(frame, state="disabled", width=10)
price3.grid(row=3, column=2)
qty3 = Entry(frame, state="disabled", width=10)
qty3.grid(row=3, column=3)
sub3 = Entry(frame, state="readonly", width=10)
sub3.grid(row=3, column=4)

# Total
Label(frame, text="Total Amount:").grid(row=4, column=3, sticky='e')
total_entry = Entry(frame, state="readonly", width=10)
total_entry.grid(row=4, column=4)

# Buttons
Button(frame, text="COMPUTE",bg="yellow", command=compute_total).grid(row=5, column=3)
Button(frame, text="CLEAR",bg="red", command=clear_all).grid(row=5, column=4)

frame.mainloop()