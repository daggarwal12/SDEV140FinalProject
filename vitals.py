import tkinter as tk
import re
from PIL import ImageTk, Image

class VitalsWindow(tk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.parent = parent
        self.data = data

        # create and display an image
        img = Image.open("vitals.png")
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(self, image=img)
        img_label.pack(pady=20)

        self.blood_pressure_label = tk.Label(self, text="Blood Pressure:")
        self.blood_pressure_label.grid(row=0, column=0)
        self.blood_pressure_var = tk.StringVar()
        self.blood_pressure_entry = tk.Entry(self, textvariable=self.blood_pressure_var)
        self.blood_pressure_entry.grid(row=0, column=1)

        self.heart_rate_label = tk.Label(self, text="Heart Rate:")
        self.heart_rate_label.grid(row=1, column=0)
        self.heart_rate_var = tk.StringVar()
        self.heart_rate_entry = tk.Entry(self, textvariable=self.heart_rate_var)
        self.heart_rate_entry.grid(row=1, column=1)

        self.oxygen_level_label = tk.Label(self, text="Oxygen Level:")
        self.oxygen_level_label.grid(row=2, column=0)
        self.oxygen_level_var = tk.StringVar()
        self.oxygen_level_entry = tk.Entry(self, textvariable=self.oxygen_level_var)
        self.oxygen_level_entry.grid(row=2, column=1)

        self.temp_label = tk.Label(self, text="Temperature:")
        self.temp_label.grid(row=3, column=0)
        self.temp_var = tk.StringVar()
        self.temp_entry = tk.Entry(self, textvariable=self.temp_var)
        self.temp_entry.grid(row=3, column=1)

        self.joint_ache_label = tk.Label(self, text="Joint Ache:")
        self.joint_ache_label.grid(row=4, column=0)
        self.joint_ache_var = tk.BooleanVar()
        self.joint_ache_checkbox = tk.Checkbutton(self, variable=self.joint_ache_var, onvalue=True, offvalue=False)
        self.joint_ache_checkbox.grid(row=4, column=1)

        self.additional_info_label = tk.Label(self, text="Additional Information:")
        self.additional_info_label.grid(row=5, column=0)
        self.additional_info_var = tk.StringVar()
        self.additional_info_entry = tk.Entry(self, textvariable=self.additional_info_var)
        self.additional_info_entry.grid(row=5, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_vitals)
        self.submit_button.grid(row=6, column=1)

        self.blood_pressure_entry.focus_set()

    def submit_vitals(self):
        if not re.match(r"^[0-9/]*$", self.blood_pressure_var.get()):
            tk.messagebox.showerror("Error", "Invalid blood pressure")
            return
        if not re.match(r"^[0-9]*$", self.heart_rate_var.get()):
            tk.messagebox.showerror("Error", "Invalid heart rate")
            return
        if not re.match(r"^[0-9]*$", self.oxygen_level_var.get()):
            tk.messagebox.showerror("Error", "Invalid oxygen level")
            return
        if not re.match(r"^[0-9.]*$", self.temp_var.get()):
            tk.messagebox.showerror("Error", "Invalid temperature")
            return

        # If validation passes, create a dictionary with the data and pass it to the parent window
        data = {
            "name": self.data["name"],
            "email": self.data["email"],
            "phone": self.data["phone"],
            "address": self.data["address"],
            "age": self.data["age"],
            "gender": self.data["gender"],
            "blood_pressure": self.blood_pressure_var.get(),
            "heart_rate": self.heart_rate_var.get(),
            "oxygen_level": self.oxygen_level_var.get(),
            "temperature": self.temp_var.get(),
            "joint_ache": self.joint_ache_var.get(),
            "additional_info": self.additional_info_var.get()
        }
        self.parent.show_confirmation(data)

