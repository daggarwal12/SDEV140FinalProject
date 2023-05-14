import tkinter as tk
from registration import RegistrationWindow
from vitals import VitalsWindow


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Medical Assistance App")
        self.root.geometry("500x500")

        self.registration_window = RegistrationWindow(self)
        self.vitals_window = VitalsWindow(self)

        self.show_registration_window()

        self.root.mainloop()

    def show_registration_window(self):
        self.vitals_window.hide()
        self.registration_window.show()

    def show_vitals_window(self):
        self.registration_window.hide()
        self.vitals_window.show()

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.run()
