import json


class Student:
    def __init__(self, name, roll_no, grades=None, attendance=0):
        self.name = name
        self.roll_no = roll_no
        self.grades = grades if grades else {}
        self.attendance = attendance

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def update_attendance(self, days):
        self.attendance += days

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "grades": self.grades,
            "attendance": self.attendance
        }


class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, roll_no):
        student = Student(name, roll_no)
        self.students.append(student.to_dict())
        self.save_students()

    def add_grade(self, roll_no, subject, grade):
        for student in self.students:
            if student["roll_no"] == roll_no:
                student["grades"][subject] = grade
                self.save_students()
                return
        print("Student not found!")

    def update_attendance(self, roll_no, days):
        for student in self.students:
            if student["roll_no"] == roll_no:
                student["attendance"] += days
                self.save_students()
                return
        print("Student not found!")

    def list_students(self):
        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Attendance: {student['attendance']} days")
            print("Grades:", student['grades'])


def student_management_system():
    system = StudentManagementSystem()

    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. Update Attendance")
        print("4. List Students")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            roll_no = input("Enter student roll number: ")
            system.add_student(name, roll_no)
        elif choice == 2:
            roll_no = input("Enter student roll number: ")
            subject = input("Enter subject name: ")
            grade = input("Enter grade: ")
            system.add_grade(roll_no, subject, grade)
        elif choice == 3:
            roll_no = input("Enter student roll number: ")
            days = int(input("Enter number of days attended: "))
            system.update_attendance(roll_no, days)
        elif choice == 4:
            system.list_students()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


student_management_system()
