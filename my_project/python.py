import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

# Connect to the SQLite database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        user_type TEXT
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            location TEXT,
            phone_number TEXT,
            disease TEXT  -- New field for disease
        )
        ''')



# Insert default doctor credentials (if not already exists)
cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, user_type) VALUES (?, ?, ?)
''', ("doc", "doc", "doctor"))

conn.commit()



class HospitalManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hospital Management System")
        self.geometry("400x300")
        
        # Set the application icon (favicon)
        self.iconbitmap('hospital.ico')  # Adjust the path to your favicon file
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (IntroPage, SignUpPage, LoginPage, PatientDashboard, DoctorDashboard, AboutPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("IntroPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)
        
        home_menu = tk.Menu(menu)
        menu.add_cascade(label="Home", menu=home_menu)
        home_menu.add_command(label="Home", command=lambda: self.show_frame("IntroPage"))
        
        about_menu = tk.Menu(menu)
        menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About", command=lambda: self.show_frame("AboutPage"))


class IntroPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#e0f7fa")
        
        # Title Label
        title_label = tk.Label(self, text="Welcome to Thakur Hospital", font=('Helvetica', 36, 'bold'), bg="#e0f7fa", fg="#00796b")
        title_label.pack(pady=0)
        
        # Hospital Image
        img = Image.open('hospital.png')  # Adjust the path to your image file
        resized = img.resize((200, 100))  # Resize to appropriate dimensions
        self.hospital_image = ImageTk.PhotoImage(resized)  # Convert to PhotoImage
        self.hospital_image_label = tk.Label(self, image=self.hospital_image, bg="#e0f7fa")
        self.hospital_image_label.pack(pady=0)
        
        # Hospital Description
        description = (
            "Thakur Hospital is dedicated to providing top-notch healthcare services to the community.\n"
            "Our team of experienced professionals is committed to delivering the best patient care.\n"
            "Explore our services, book appointments, and manage your health with ease."
        )
        description_label = tk.Label(self, text=description, font=('Helvetica', 16), bg="#e0f7fa", fg="#004d40", wraplength=800, justify="center")
        description_label.pack(pady=20, padx=20)
        
        # Buttons
        button_frame = tk.Frame(self, bg="#e0f7fa")
        button_frame.pack(pady=30)

        tk.Button(button_frame, text="Login", font=('Helvetica', 18), width=20, height=2, bg="#00796b", fg="white", borderwidth=0, relief="flat", command=lambda: controller.show_frame("LoginPage")).pack(pady=10)
        tk.Button(button_frame, text="Sign Up", font=('Helvetica', 18), width=20, height=2, bg="#004d40", fg="white", borderwidth=0, relief="flat", command=lambda: controller.show_frame("SignUpPage")).pack(pady=10)
        
        # Footer
        footer_frame = tk.Frame(self, bg="#e0f7fa")
        footer_frame.pack(side="bottom", pady=20)
        
        tk.Label(footer_frame, text="thakur Hospital © 2024", font=('Helvetica', 12), bg="#e0f7fa", fg="#004d40").pack()

        # Ensure the layout resizes correctly
        self.pack(fill="both", expand=True)


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#f5f5f5")

        # Title
        tk.Label(self, text="Sign Up", font=('Helvetica', 24, 'bold'), bg="#f5f5f5", fg="#004d40").pack(pady=20)

        # Username Entry
        tk.Label(self, text="Username", font=('Helvetica', 14), bg="#f5f5f5", fg="#00796b").pack(pady=5)
        self.username_entry = tk.Entry(self, font=('Helvetica', 14))
        self.username_entry.pack(pady=5)

        # Password Entry
        tk.Label(self, text="Password", font=('Helvetica', 14), bg="#f5f5f5", fg="#00796b").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=('Helvetica', 14))
        self.password_entry.pack(pady=5)

        # Sign Up Button
        tk.Button(self, text="Sign Up", font=('Helvetica', 14), bg="#00796b", fg="white", command=self.sign_up).pack(pady=20)

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        try:
            cursor.execute("INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)", (username, password, "patient"))
            conn.commit()
            messagebox.showinfo("Success", "Sign Up Successful! Redirecting to Home Page.")
            self.controller.show_frame("IntroPage")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#f5f5f5")

        # Title
        tk.Label(self, text="Login", font=('Helvetica', 24, 'bold'), bg="#f5f5f5", fg="#004d40").pack(pady=20)

        # Username Entry
        tk.Label(self, text="Username", font=('Helvetica', 14), bg="#f5f5f5", fg="#00796b").pack(pady=5)
        self.username_entry = tk.Entry(self, font=('Helvetica', 14))
        self.username_entry.pack(pady=5)

        # Password Entry
        tk.Label(self, text="Password", font=('Helvetica', 14), bg="#f5f5f5", fg="#00796b").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=('Helvetica', 14))
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(self, text="Login", font=('Helvetica', 14), bg="#00796b", fg="white", command=self.check_login).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        
        if result:
            user_type = result[2]  # "patient" or "doctor"
            if user_type == "patient":
                self.controller.show_frame("PatientDashboard")
            else:
                self.controller.show_frame("DoctorDashboard")
        else:
            messagebox.showerror("Error", "Invalid Credentials")


class PatientDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#e0f7fa")
        
        # Title
        tk.Label(self, text="Patient Dashboard", font=('Helvetica', 24, 'bold'), bg="#e0f7fa", fg="#00796b").pack(pady=20)
        
        # Frame for patient information
        info_frame = tk.Frame(self, bg="#e0f7fa")
        info_frame.pack(side="left", padx=20, pady=20, fill="y")
        
        # Patient Information Entries
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.location_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.disease_var = tk.StringVar()  # New field for disease
        
        self.create_label_with_entry(info_frame, "Name:", self.name_var, 30).pack(pady=5, anchor="w")
        self.create_label_with_entry(info_frame, "Age:", self.age_var, 30).pack(pady=5, anchor="w")
        self.create_label_with_entry(info_frame, "Gender:", self.gender_var, 30).pack(pady=5, anchor="w")
        self.create_label_with_entry(info_frame, "Location:", self.location_var, 30).pack(pady=5, anchor="w")
        self.create_label_with_entry(info_frame, "Phone Number:", self.phone_var, 30).pack(pady=5, anchor="w")
        self.create_label_with_entry(info_frame, "Disease:", self.disease_var, 30).pack(pady=5, anchor="w")  # New field for disease

        # Submit Button
        submit_frame = tk.Frame(self, bg="#e0f7fa")
        submit_frame.pack(side="left", padx=20, pady=20)
        tk.Button(submit_frame, text="Submit", font=('Helvetica', 14), bg="#00796b", fg="white", command=self.submit).pack(pady=20)
        
        # Add image on the right side
        self.image = Image.open('doctor.png')  # Adjust path to your image file
        self.image = self.image.resize((350, 500))  # Resize to fit the layout
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.image_label = tk.Label(self, image=self.photo, bg="#e0f7fa")
        self.image_label.pack(side="right", padx=20)

    def create_label_with_entry(self, parent, label_text, text_variable, entry_width):
        frame = tk.Frame(parent, bg="#e0f7fa")
        label = tk.Label(frame, text=label_text, font=('Helvetica', 12), bg="#e0f7fa", fg="#004d40")
        entry = tk.Entry(frame, textvariable=text_variable, width=entry_width, font=('Helvetica', 12))
        
        label.pack(side="left", padx=5)
        entry.pack(side="left", padx=5)
        
        return frame
    
    def submit(self):
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        location = self.location_var.get()
        phone_number = self.phone_var.get()
        disease = self.disease_var.get()  # New field for disease
        
        if not (name and age and gender and location and phone_number and disease):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        
        # Insert data into the table
        cursor.execute('''
        INSERT INTO patients (name, age, gender, location, phone_number, disease)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, age, gender, location, phone_number, disease))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Patient information submitted successfully.")
        self.clear_fields()

    def clear_fields(self):
        # Clear all entry fields after submission
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.location_var.set("")
        self.phone_var.set("")
        self.disease_var.set("")  # Clear the disease field


class DoctorDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.current_index = 0
        
        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#e0f7fa")
        
        # Title
        tk.Label(self, text="Doctor Dashboard", font=('Helvetica', 36, 'bold'), bg="#e0f7fa", fg="#00796b").pack(pady=20)
        
        # Appointment Details
        self.details_label = tk.Label(self, text="", font=('Helvetica', 16), bg="#e0f7fa", fg="#004d40", wraplength=800)
        self.details_label.pack(pady=20, padx=20)
        
        # Buttons
        button_frame = tk.Frame(self, bg="#e0f7fa")
        button_frame.pack(pady=20, padx=20, fill="x")
        
        tk.Button(button_frame, text="Next Appointment", font=('Helvetica', 14), bg="#00796b", fg="white", command=self.show_next_appointment, width=20).pack(side="left", padx=10)
        tk.Button(button_frame, text="Logout", font=('Helvetica', 14), bg="#004d40", fg="white", command=lambda: self.controller.show_frame("IntroPage"), width=20).pack(side="right", padx=10)
    
    def show_next_appointment(self):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        
        if patients and self.current_index < len(patients):
            patient = patients[self.current_index]
            details = (
                f"Patient: {patient[1]}\n"
                f"Disease: {patient[6]}\n"  # Assuming disease is in the 7th column
                f"Age: {patient[2]}\n"
                f"Gender: {patient[3]}"
            )
            self.details_label.config(text=details)
            self.current_index += 1
        else:
            messagebox.showinfo("End", "No more patients.")
        
        conn.close()


class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.controller.create_menu()
        
        # Background color
        self.configure(bg="#f1f8e9")
        
        # Title
        tk.Label(self, text="About Us", font=('Helvetica', 24, 'bold'), bg="#f1f8e9", fg="#004d40").pack(pady=20)
        
        # Subtitle
        tk.Label(self, text="Meet the Team", font=('Helvetica', 18), bg="#f1f8e9", fg="#00796b").pack(pady=10)
        
        # Team Members with resized images
        team_frame = tk.Frame(self, bg="#f1f8e9")
        team_frame.pack(pady=20)
        
        self.create_team_member(team_frame, "Ujwal Sahu", "hospital.png").pack(pady=10)
        self.create_team_member(team_frame, "Ritesh", "hospital.png").pack(pady=10)
        self.create_team_member(team_frame, "Yash", "hospital.png").pack(pady=10)
        
        # Back Button
        tk.Button(self, text="Back to Home", font=('Helvetica', 14), bg="#00796b", fg="white", command=lambda: self.controller.show_frame("IntroPage")).pack(pady=20)

    def create_team_member(self, parent_frame, name, photo_path):
        frame = tk.Frame(parent_frame, bg="#f1f8e9")
        
        # Load and resize the image
        image = Image.open(photo_path)
        image = image.resize((50, 50))  # Resize to 50x50 pixels
        photo = ImageTk.PhotoImage(image)
        
        # Team member layout
        tk.Label(frame, text=name, font=('Helvetica', 14), bg="#f1f8e9", fg="#004d40").pack(side="left", padx=10)
        tk.Label(frame, image=photo, bg="#f1f8e9").pack(side="left")
        frame.photo = photo  # Keep a reference to avoid garbage collection
        
        return frame


if __name__ == "__main__":
    app = HospitalManagementSystem()
    app.mainloop()
    conn.close()
