Generate an entity-relationship diagram (ERD) for an SQL database based on the descriptions of the following tables:

### Tables and Their Attributes:

1. **Teacher Table**  
   - `teacher_id` (Primary Key)  
   - `name` (Teacher's name)  
   - `email` (Teacher’s email — unique)  
   - `password` (Hashed password)  
   - `subject` (Subject taught by the teacher)

2. **Class Table**  
   - `class_id` (Primary Key)  
   - `class_name` (Class name, e.g., "2Q1")  
   - `teacher_id` (Foreign Key from Teacher)

3. **AttendanceSheet Table**  
   - `attendance_id` (Primary Key)  
   - `sheet_name` (Name of the attendance sheet, e.g., "Math Class - 2Q1")  
   - `class_id` (Foreign Key from Class)  
   - `qr_code` (URL/QR code string)  
   - `date` (Date of the attendance session)  
   - `student_name` (Name of the student)  
   - `roll_no` (Roll number of the student)  
   - `student_class` (The class the student is attending)  
   - `status` (Present/Absent — based on the student's selection)

4. **Teacher_AttendanceSheet Linking Table**  
   - `teacher_id` (Foreign Key from Teacher)  
   - `attendance_id` (Foreign Key from AttendanceSheet)  
   - **Primary Key** (`teacher_id`, `attendance_id`)

### Relationships:  
- One `Teacher` can teach multiple `Classes`.  
- Each `Class` has one `Teacher`, establishing a one-to-many relationship.  
- Each `Class` can have multiple `AttendanceSheets`, establishing a one-to-many relationship.  
- Each `AttendanceSheet` is linked to multiple `Teachers` through the linking table, establishing a many-to-many relationship.

Create the ERD using this structure, clearly indicating primary and foreign keys, along with the relationships between the tables. Include all attributes for each table in the ERD.
