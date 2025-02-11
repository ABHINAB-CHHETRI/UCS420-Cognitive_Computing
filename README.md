Project Title: Attendance Management System (SQL-based)

Objective:
I want to build a web-based Attendance Management System for teachers and students. The system will have two main components:
1. Teacher Portal: Teachers can create attendance sheets, assign classes, and generate QR codes for students.
2. Student Portal: Students will scan the QR code, fill in their attendance by entering their name, roll number, and selecting their class.

The main goal is to track attendance records for each student without requiring students to log in, and for teachers to easily manage and view those records.

Components Overview:

1. Teacher Portal:
   - Teachers will log in with their credentials (name, email, password) and will be authenticated using a hashed password.
   - Teachers will have the ability to create an attendance sheet where they can:
     - Assign a class (e.g., 2Q1, 2Q2, etc.).
     - Enter a name for the attendance sheet (e.g., "Math Class - 2Q1").
     - Generate a unique QR code that links to a form for students to fill out their attendance.

2. Student Portal:
   - Students will scan the generated QR code, which will redirect them to a form.
   - The form will ask the student to input:
     - Name (Student’s full name).
     - Roll number (Student’s roll number).
     - Class (e.g., 2Q1, 2Q2).
     - Status (Present or Absent — This will be automatically marked when the student submits the form).

3. Backend Logic:
   - The backend will handle authentication for teachers, attendance sheet creation, and storing attendance data for students.
   - The attendance data will be saved in an SQL database, and students will not be required to log in. They just need to fill out the form with their details when they scan the QR code.

Database Design (SQL):
I will use MySQL for this project. Here's the database structure I have in mind:

1. Teacher Table:
   - Attributes:
     - teacher_id (Primary Key)
     - name (Teacher's name)
     - email (Teacher’s email — unique)
     - password (Hashed password)
     - subject (Subject taught by the teacher)

2. Class Table:
   - Attributes:
     - class_id (Primary Key)
     - class_name (Class name, e.g., "2Q1")
     - teacher_id (Foreign Key from Teacher)

3. AttendanceSheet Table:
   - Attributes:
     - attendance_id (Primary Key)
     - sheet_name (Name of the attendance sheet, e.g., "Math Class - 2Q1")
     - class_id (Foreign Key from Class)
     - qr_code (URL/QR code string)
     - date (Date of the attendance session)
     - student_name (Name of the student)
     - roll_no (Roll number of the student)
     - student_class (The class the student is attending)
     - status (Present/Absent — based on the student's selection)

4. Teacher_AttendanceSheet Linking Table:
   - Attributes:
     - teacher_id (Foreign Key from Teacher)
     - attendance_id (Foreign Key from AttendanceSheet)
     - Primary Key (teacher_id, attendance_id)

   This table links Teachers with the AttendanceSheets they created. A teacher can have multiple attendance sheets, and each attendance sheet is tied to one teacher.

Flow of the System:
1. Teacher Creates an Attendance Sheet:
   - The teacher logs in and creates an attendance sheet, associating it with a class (e.g., 2Q1) and giving it a name.
   - The system generates a unique QR code for the attendance sheet.
   - The teacher’s Teacher_AttendanceSheet table entry is updated with the generated attendance_id for that sheet.

2. Student Fills Out the Attendance Form:
   - Students scan the QR code, which takes them to a form.
   - The form asks for their name, roll number, and class. They also select whether they are "Present" or "Absent."
   - The attendance data is submitted and stored in the AttendanceSheet table, including student details and their attendance status (Present/Absent).

3. Teacher Views Attendance Records:
   - The teacher can view all the attendance sheets they’ve created, and the system will fetch the attendance data from the AttendanceSheet table using the Teacher_AttendanceSheet linking table.

Key Requirements:
- Authentication: Teachers will log in with a secure, hashed password.
- QR Code Generation: After the teacher creates an attendance sheet, a unique QR code will be generated for the sheet.
- Database: I will use MySQL to store the data, with the following tables: Teacher, Class, AttendanceSheet, and Teacher_AttendanceSheet.
- Frontend: I will use EJS for rendering dynamic HTML views and Node.js as the backend to handle all API calls and logic.

Task Requests:
1. Backend Setup:
   - Help me set up the Node.js backend to handle teacher login, creating attendance sheets, and storing attendance data.
   
2. Database Structure:
   - Review the database schema to ensure everything is well-designed for relational SQL.
   
3. QR Code Generation:
   - Assist with how to generate and display the QR code for the attendance sheet, linking it to the corresponding attendance form.

4. Frontend Form:
   - Help me with the form where students will input their details (name, roll number, class) and select their attendance status (Present/Absent).
   - Explain how the form can validate the input and submit the data back to the backend.

5. Teacher Dashboard:
   - Guide me through building a simple teacher dashboard to display all attendance records linked to their account.

This is a general overview of the project. I need assistance with the backend and API development, as well as making sure the entire system is working seamlessly. Could you help me with that?
