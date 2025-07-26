# Employee-Management-system
 🧑‍💼 Employee Management System (Tkinter + MySQL)

A desktop GUI application to manage employee records using Python's Tkinter for the interface and MySQL as the backend database.


 📌 Features

- Add new employees
- Update employee details
- Delete employee records
- Search employees by ID, Name, or Contact
- View all employee data in a table
- Fields include:
  - Employee ID
  - Name
  - Email
  - Gender
  - Contact
  - Date of Birth
  - Address
  - Department
  - Joining Date
  - Salary



 🛠 Tech Stack

- Python: Tkinter (GUI)
- Database: MySQL
- Library: `pymysql` for Python-MySQL connection



 ⚙️ How to Set Up and Run

 ✅ 1. Clone the Repository


git clone https://github.com/your-username/Employee-Management-system.git
cd Employee-Management-system

✅ 2. Install Dependencies
Make sure you have pymysql installed:

pip install pymysql

✅ 3. Set Up the MySQL Database
Open MySQL.

Create the database and table:

CREATE DATABASE EMS;
USE EMS;
CREATE TABLE Employee2 (
    eid INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender VARCHAR(10),
    Contact VARCHAR(20),
    dob DATE,
    Address TEXT,
    department VARCHAR(100),
    joining_date DATE,
    salary FLOAT
);
Update your MySQL credentials in the code if needed (e.g., user="root", password="your_password").

✅ 4. Run the Application


python main.py
The application window should open, allowing you to add and manage employee records.

📁 File Structure

Employee-Management-system/
│
├── main.py         # Main Python script
├── README.md       # Project documentation
└── ..

🛡️ Notes
Make sure MySQL is running when using the app.

You can customize the theme, add validations, or implement export-to-CSV as enhancements.

Passwords in the code should be managed securely (avoid hardcoding in real-world apps).

👨‍💻 Developed By
🚀 Aditya Raut
📌 [Aditya Raut - GitHub Profile](https://github.com/Adityaraut67)


 🚀 Future Enhancements

Here are some planned or possible improvements to expand the functionality and usability of the application:

- ✅Login System  
  Add user authentication (admin/staff roles) to restrict access to employee data.

- ✅Export to Excel/CSV
  Allow exporting employee records into CSV or Excel formats for reports and backups.

- ✅Search Filters & Sorting 
  Advanced filters (by department, date range, salary range) and table column sorting.

- ✅Image Upload  
  Enable uploading and displaying employee profile pictures.

- ✅PDF Report Generation  
  Generate printable PDF reports of employee data using libraries like `reportlab` or `fpdf`.

- ✅Data Validation 
  Add robust input validation (e.g., email format, contact number length, salary range).
