import tkinter as tk
import re

class RegistrationWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(self, textvariable=self.email_var)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.grid(row=2, column=0)
        self.phone_var = tk.StringVar()
        self.phone_entry = tk.Entry(self, textvariable=self.phone_var)
        self.phone_entry.grid(row=2, column=1)

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_var = tk.StringVar()
        self.address_entry = tk.Entry(self, textvariable=self.address_var)
        self.address_entry.grid(row=3, column=1)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.grid(row=4, column=0)
        self.age_var = tk.StringVar()
        self.age_entry = tk.Entry(self, textvariable=self.age_var)
        self.age_entry.grid(row=4, column=1)

        self.gender_label = tk.Label(self, text="Gender:")
        self.gender_label.grid(row=5, column=0)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.gender_menu = tk.OptionMenu(self, self.gender_var, "Male", "Female", "Other")
        self.gender_menu.grid(row=5, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_registration)
        self.submit_button.grid(row=6, column=1)

        self.name_entry.focus_set()

    def submit_registration(self):
        if not re.match(r"^[a-zA-Z ]*$", self.name_var.get()):
            tk.messagebox.showerror("Error", "Invalid name")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_var.get()):
            tk.messagebox.showerror("Error", "Invalid email")
            return
        if not re.match(r"^[0-9]*$", self.phone_var.get()):
            tk.messagebox.showerror("Error", "Invalid phone number")
            return
        if not re.match(r"^[0-9]*$", self.age_var.get()):
            tk.messagebox.showerror("Error", "Invalid age")
            return

        # If validation passes, create a dictionary with the data and pass it to the parent window
        data = {
            "name": self.name_var.get(),
            "email": self.email_var.get(),
            "phone": self.phone_var.get(),
            "address": self.address_var.get(),
            "age": self.age_var.get(),
            "gender": self.gender_var.get()
        }
        self.parent.show_vitals_window(data)

