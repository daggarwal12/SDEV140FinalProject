import tkinter as tk

class RegistrationWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registration")

        # I tried adding an image here, even used import PTI as image code but since the code kept coming back with error, I removed the code. I tired at vitals as well. Did not work.
        
        # Name
        tk.Label(self, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)
        
        # Email
        tk.Label(self, text="Email").grid(row=1, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1)
        
        # Phone Number
        tk.Label(self, text="Phone Number").grid(row=2, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1)
        
        # Address
        tk.Label(self, text="Address").grid(row=3, column=0)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1)
        
        # Age
        tk.Label(self, text="Age").grid(row=4, column=0)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=4, column=1)
        
        # Gender
        tk.Label(self, text="Gender").grid(row=5, column=0)
        self.gender_var = tk.StringVar(self)
        self.gender_var.set("Male")
        self.gender_menu = tk.OptionMenu(self, self.gender_var, "Male", "Female", "Other")
        self.gender_menu.grid(row=5, column=1)
        
        # Submit Button
        tk.Button(self, text="Submit", command=self.submit_registration).grid(row=6, column=1)
        
    def submit_registration(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_entry.get()
        address = self.address_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        
        # Perform validation here
        
        # If validation passes, close registration window and open vitals window
        self.destroy()
        VitalsWindow(name, email, phone_number, address, age, gender)
        # my cancel button did not show up. I tried changing the code 4 different ways.

class VitalsWindow(tk.Toplevel):
    def __init__(self, name, email, phone_number, address, age, gender):
        super().__init__()
        self.title("Vitals")
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.age = age
        self.gender = gender
        
        # Blood Pressure
        tk.Label(self, text="Blood Pressure").grid(row=0, column=0)
        self.bp_entry = tk.Entry(self)
        self.bp_entry.grid(row=0, column=1)
        
        # Heart Rate
        tk.Label(self, text="Heart Rate").grid(row=1, column=0)
        self.hr_entry = tk.Entry(self)
        self.hr_entry.grid(row=1, column=1)
        
        # Oxygen Level
        tk.Label(self, text="Oxygen Level").grid(row=2, column=0)
        self.oxygen_entry = tk.Entry(self)
        self.oxygen_entry.grid(row=2, column=1)
        
        # Temperature
        tk.Label(self, text="Temperature").grid(row=3, column=0)
        self.temp_entry = tk.Entry(self)
        self.temp_entry.grid(row=3, column=1)
        
        # Sugar
        tk.Label(self, text="Sugar").grid(row=4, column=0)
        self.sugar_entry = tk.Entry(self)
        self.sugar_entry.grid(row=4, column=1)
        
        # Joint Ache
        tk.Label(self, text="Joint Ache").grid(row=5, column=0)
        self.joint_ache_var = tk.BooleanVar(self)
        self.joint_ache_var.set(False)
        self.joint_ache_yes_radio = tk.Radiobutton(self, text="Yes", variable=self.joint_ache_var, value=True)
        self.joint_ache_yes_radio.grid(row=5, column=1)
        self.joint_ache_no_radio = tk.Radiobutton(self, text="No", variable=self.joint_ache_var, value=False)
        self.joint_ache_no_radio.grid(row=5, column=2)
        
        # Additional Information
        tk.Label(self, text="Additional Information").grid(row=6, column=0)
        self.additional_info_text = tk.Text(self, height=5, width=30)
        self.additional_info_text.grid(row=6, column=1)
        
        # Submit Button
        tk.Button(self, text="Submit", command=self.submit_vitals).grid(row=7, column=1)
        
    def submit_vitals(self):
        blood_pressure = self.bp_entry.get()
        heart_rate = self.hr_entry.get()
        oxygen_level = self.oxygen_entry.get()
        temperature = self.temp_entry.get()
        sugar = self.sugar_entry.get()
        joint_ache = self.joint_ache_var.get()
        additional_info = self.additional_info_text.get("1.0", "end-1c")
        
        # Perform validation here
        
        # If validation passes, close vitals window and show confirmation message
        self.destroy()
        confirmation_window = tk.Toplevel()
        confirmation_window.title("Confirmation")
        confirmation_message = f"Name: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nAge: {self.age}\nGender: {self.gender}\n\nVitals:\nBlood Pressure: {blood_pressure}\nHeart Rate: {heart_rate}\nOxygen Level: {oxygen_level}\nTemperature: {temperature}\nSugar: {sugar}\nJoint Ache: {'Yes' if joint_ache else 'No'}\n\nAdditional Information:\n{additional_info}"
        tk.Label(confirmation_window, text=confirmation_message).grid(row=0, column=0)

        # Check blood pressure
        blood_pressure = int(blood_pressure)
        if 80 <= blood_pressure <= 120:
            print("Your blood pressure is normal.")
        elif 120 <= blood_pressure <= 139:
            print("Your blood pressure is at risk.")
        else:
            print("I advise you to get it checked.")

        # Check sugar level
        sugar = int(sugar)
        if sugar <= 99:
            print("Your sugar levels are normal.")
        elif 100 <= sugar <= 125:
            print("You might have prediabetes.")
        else:
            print("I advise you to please get it checked.")

        # Check temperature
        temperature = int(temperature)
        if 96 <= temperature <= 99:
            print("Your temperature is adequate.")
        elif temperature <= 95:
            print("You are at risk for hypothermia.")
        else:
            print("I advise you to get it checked.")

        # Check overall health
        if 80 <= blood_pressure <= 120 and sugar <= 99 and 96 <= temperature <= 99:
            print("You are healthy! Congratulations!")
        else:
            print("Please consider going to the hospital.")

        # Print out information for testing purposes
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)
        print("Address:", self.address)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Blood Pressure:", blood_pressure)
        print("Heart Rate:", heart_rate)
        print("Oxygen Level:", oxygen_level)
        print("Temperature:", temperature)
        print("Sugar Level:", sugar)
        print("Joint Ache:", joint_ache)
        print("Additional Information:", additional_info)
        
if __name__ == "__main__":
    registration_window = RegistrationWindow()
    registration_window.mainloop()
