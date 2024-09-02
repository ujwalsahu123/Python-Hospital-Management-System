<h1>Hospital Management System using python and gui</h1>
<hr>
<img src='Screenshot 2024-08-18 234235.png' >


<hr>

<h2>Project Overview</h2>
This project is a Hospital Management System developed using Python’s tkinter library for the GUI, alongside an SQLite database for managing patient and user data. The system includes functionalities for user registration, patient information management, and a doctor dashboard to handle appointments.
<br>
<hr>
**Problem Statement:**
Small clinics often struggle with inefficient and error-prone manual processes for managing patient records, appointments, and communication. These challenges can lead to delays, data inaccuracies, and poor patient experiences. The goal is to develop a digital solution that automates and streamlines these processes, ensuring accurate record-keeping, timely appointments, and improved overall clinic management.
<hr>
<h2>Features</h2>
User Authentication: Allows users to sign up and log in securely.
<br>
Patient Dashboard: Collects patient details like name, age, gender, location, and phone number, along with the disease description.
<br>
Doctor Dashboard: Displays patient appointments, including details like patient name, age, gender, location, and disease.
<br>
User Management: Uses SQLite database to store and retrieve user and patient information.
<br>
Navigation Menu: Allows easy navigation between the Home and About pages.
<br>
<hr>
<br>
Technologies Used
<br>
Python: Core language used for logic and GUI.
<br>
tkinter: Python’s built-in library for creating the graphical user interface (GUI).
<br>
SQLite: Lightweight database used for data storage.
<br>
PIL (Pillow): Used for image processing in the GUI.
<br>
<hr>
<img src='Screenshot 2024-08-21 145253.png' >
Project Structure
Intro Page: Provides an overview of the system and options to log in or sign up.<br>
Sign Up Page: Allows new users to register with their username and password.<br>
Login Page: Authenticates users based on credentials.<br>
Patient Dashboard: Allows patients to enter and submit their details.<br>
Doctor Dashboard: Allows doctors to view patient information and manage appointments.<br>
About Page: Includes details about the project team, with links to the GitHub repository.<br>
<br>
<hr>
<br>
User Registration:
<br>
Users sign up with a username and password, which is stored in the users table in the SQLite database.<br>

Patient Information:<br>
Patients submit their details (name, age, gender, location, phone number, disease) via the patient dashboard. This information is stored in the patients table.<br>

Doctor Dashboard:<br>
The doctor can view appointments and patient details, retrieved from the patients table.<br>

Login Validation:<br>
During login, the system checks user credentials against the data stored in the users table to determine whether access is granted.

<hr>
<h2>steps to run the application :</h2>
1 folk this repo to your github <br>
2 open vscode and and clone your folked repo or this original repo by -> terminal -> git clone (https:...link..) <br>
3 install python and also intall necessary libraries using the treminal<br>
4  for Running the applications:<br>
 Navigate to the project directory:*** you need to be in that folder in the terminal cmd line -> cd Pyhon-Hospital-Management-System<br>
 *** in vscode run the application by right clicking on the python.py file -> Run python file in the terminal (option) <br>
5 use chatgpt for help .<br>
6 download sql lite for database viewing .
<img src='Screenshot 2024-08-21 145200.png' >
<hr>
Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
<hr>
License<br>
This project is licensed under the MIT License.
