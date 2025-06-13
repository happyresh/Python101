# Contributors: Gatchalian, Recio, Latoy, Urbano
# Date: June 01, 2025
# Integrative Programming - Tkinter Programming Task #4

import tkinter as tk
from tkinter import messagebox, ttk

class JollyMcKingOrderSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jolly McKing Order System")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(bg="#f7f7f7")

        self.option_add("*Font", "Arial 12")

        header = tk.Label(self, text="Jolly McKing Order System", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#2d3436")
        header.pack(pady=(18, 10))

        login_frame = tk.LabelFrame(self, text="Login", font=("Arial", 13, "bold"), bg="#f7f7f7", fg="#636e72", bd=2, relief="groove", padx=15, pady=10)
        login_frame.pack(padx=30, pady=(0, 18), fill="x")
        login_frame.grid_columnconfigure(4, weight=1)  

        tk.Label(login_frame, text="Username:", bg="#f7f7f7").grid(row=0, column=0, sticky="e", padx=(0, 5), pady=3)
        self.username_entry = tk.Entry(login_frame, width=14)
        self.username_entry.grid(row=0, column=1, padx=(0, 15), pady=3)
        tk.Label(login_frame, text="Password:", bg="#f7f7f7").grid(row=0, column=2, sticky="e", padx=(0, 5), pady=3)
        self.password_entry = tk.Entry(login_frame, width=14, show="*")
        self.password_entry.grid(row=0, column=3, padx=(0, 10), pady=3)
        self.ok_button = tk.Button(login_frame, text="Ok", bg="#0984e3", fg="white", width=12, command=self.login)
        self.ok_button.grid(row=0, column=4, padx=(0, 0), pady=3, sticky="ew")

        self.order_frame = tk.LabelFrame(self, text="Order Details", font=("Arial", 14, "bold"), bg="#f7f7f7", fg="#636e72", bd=2, relief="groove", padx=18, pady=12)
        self.order_frame.pack(padx=30, pady=(0, 10), fill="x")
        self.order_frame.config(labelanchor="n")

        meal1_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        meal1_row.pack(anchor="center", pady=4)
        tk.Label(meal1_row, text="Value Meal #1:", bg="#f7f7f7", width=15, anchor="w").pack(side="left")
        tk.Label(meal1_row, text="P25.00", bg="#f7f7f7", fg="#00b894", width=8, anchor="w").pack(side="left")
        tk.Label(meal1_row, text="Qty:", bg="#f7f7f7").pack(side="left", padx=(10,0))
        self.qty_meal1 = tk.Entry(meal1_row, width=5, justify="center")
        self.qty_meal1.insert(0, "0")
        self.qty_meal1.pack(side="left", padx=(2,0))

        meal2_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        meal2_row.pack(anchor="center", pady=4)
        tk.Label(meal2_row, text="Value Meal #2:", bg="#f7f7f7", width=15, anchor="w").pack(side="left")
        tk.Label(meal2_row, text="P30.00", bg="#f7f7f7", fg="#00b894", width=8, anchor="w").pack(side="left")
        tk.Label(meal2_row, text="Qty:", bg="#f7f7f7").pack(side="left", padx=(10,0))
        self.qty_meal2 = tk.Entry(meal2_row, width=5, justify="center")
        self.qty_meal2.insert(0, "0")
        self.qty_meal2.pack(side="left", padx=(2,0))

        meal3_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        meal3_row.pack(anchor="center", pady=4)
        tk.Label(meal3_row, text="Value Meal #3:", bg="#f7f7f7", width=15, anchor="w").pack(side="left")
        tk.Label(meal3_row, text="P35.00", bg="#f7f7f7", fg="#00b894", width=8, anchor="w").pack(side="left")
        self.meal3_drink = ttk.Combobox(meal3_row, values=["Coke", "Royal", "Sprite"], width=8, state="readonly")
        self.meal3_drink.current(0)
        self.meal3_drink.pack(side="left", padx=(10, 5))
        tk.Label(meal3_row, text="Qty:", bg="#f7f7f7").pack(side="left")
        self.qty_meal3 = tk.Entry(meal3_row, width=5, justify="center")
        self.qty_meal3.insert(0, "0")
        self.qty_meal3.pack(side="left", padx=(2,0))

        rice_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        rice_row.pack(anchor="center", pady=4)
        self.extra_rice_var = tk.StringVar()
        self.extra_rice_radio = tk.Radiobutton(rice_row, text="Extra Rice", variable=self.extra_rice_var, value="yes", bg="#f7f7f7")
        self.no_extra_rice_radio = tk.Radiobutton(rice_row, text="No Extra Rice", variable=self.extra_rice_var, value="no", bg="#f7f7f7")
        self.extra_rice_radio.pack(side="left")
        self.no_extra_rice_radio.pack(side="left", padx=(10,0))
        tk.Label(rice_row, text="Qty:", bg="#f7f7f7").pack(side="left", padx=(10,0))
        self.qty_rice = tk.Entry(rice_row, width=5, justify="center")
        self.qty_rice.insert(0, "0")
        self.qty_rice.pack(side="left", padx=(2,0))
        self.extra_rice_var.set("no")

        compute_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        compute_row.pack(anchor="center", pady=(12, 4))
        self.compute_button = tk.Button(compute_row, text="Compute", bg="#00b894", fg="white", width=12, command=self.compute)
        self.compute_button.pack(anchor="center")

        total_row = tk.Frame(self.order_frame, bg="#f7f7f7")
        total_row.pack(anchor="center", pady=(10, 2))
        tk.Label(total_row, text="Total Bill is:", bg="#f7f7f7", font=("Arial", 12, "bold")).pack(side="left")
        self.total_bill = tk.Entry(total_row, width=16, state="readonly", justify="center", font=("Arial", 12, "bold"))
        self.total_bill.pack(side="left", padx=(8,0))

        bottom_row = tk.Frame(self, bg="#f7f7f7")
        bottom_row.pack(pady=(10, 8))
        self.clear_button = tk.Button(bottom_row, text="Clear", bg="#fdcb6e", fg="black", width=10, command=self.clear)
        self.clear_button.pack(side="left", padx=18)
        self.close_button = tk.Button(bottom_row, text="Close", bg="#d63031", fg="white", width=10, command=self.close)
        self.close_button.pack(side="left", padx=18)

        self.set_order_panel_enabled(False)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "123":
            self.bell()
            self.set_order_panel_enabled(True)
            self.username_entry.config(state="disabled")
            self.password_entry.config(state="disabled")
            self.ok_button.config(state="disabled")
            messagebox.showinfo("Success", "Login successful!")
        else:
            self.bell()
            messagebox.showerror("Error", "Invalid Username or Password")
            self.set_order_panel_enabled(False)

    def compute(self):
        try:
            qty1 = int(self.qty_meal1.get())
            qty2 = int(self.qty_meal2.get())
            qty3 = int(self.qty_meal3.get())
            qty_rice = int(self.qty_rice.get()) if self.extra_rice_var.get() == "yes" else 0
            if qty1 < 0 or qty2 < 0 or qty3 < 0 or (self.extra_rice_var.get() == "yes" and qty_rice < 0):
                raise ValueError
            total = 25.0 * qty1 + 30.0 * qty2 + 35.0 * qty3
            if self.extra_rice_var.get() == "yes":
                total += 25.0 * qty_rice
            self.total_bill.config(state="normal")
            self.total_bill.delete(0, tk.END)
            self.total_bill.insert(0, f"P{total:.2f}")
            self.total_bill.config(state="readonly")
        except Exception:
            messagebox.showerror("Error", "Invalid Input!")

    def clear(self):
        self.bell()
        result = messagebox.askyesno("Confirm", "Are you sure you want to clear?")
        if result:
            self.qty_meal1.delete(0, tk.END)
            self.qty_meal1.insert(0, "0")
            self.qty_meal2.delete(0, tk.END)
            self.qty_meal2.insert(0, "0")
            self.qty_meal3.delete(0, tk.END)
            self.qty_meal3.insert(0, "0")
            self.meal3_drink.current(0)
            self.extra_rice_var.set("no")
            self.qty_rice.delete(0, tk.END)
            self.qty_rice.insert(0, "0")
            self.total_bill.config(state="normal")
            self.total_bill.delete(0, tk.END)
            self.total_bill.config(state="readonly")

    def close(self):
        self.bell()
        result = messagebox.askyesno("Confirm", "Are you sure you want to exit?")
        if result:
            self.destroy()

    def set_order_panel_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        for widget in [
            self.qty_meal1, self.qty_meal2, self.qty_meal3, self.meal3_drink,
            self.extra_rice_radio, self.no_extra_rice_radio, self.qty_rice,
            self.compute_button, self.clear_button
        ]:
            widget.config(state=state)

        self.total_bill.config(state="readonly" if enabled else "disabled")

if __name__ == "__main__":
    app = JollyMcKingOrderSystem()
    app.mainloop()
