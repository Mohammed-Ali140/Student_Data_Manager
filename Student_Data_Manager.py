class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        self.students[roll_no] = Student(roll_no, name, marks)
        print("Student Added Successfully!")

    def search_student(self):
        roll_no = int(input("Enter Roll No to Search: "))
        if roll_no in self.students:
            self.students[roll_no].display()
        else:
            print("Student Not Found!")

    def update_student(self):
        roll_no = int(input("Enter Roll No to Update: "))
        if roll_no in self.students:
            name = input("Enter New Name: ")
            marks = float(input("Enter New Marks: "))

            self.students[roll_no].name = name
            self.students[roll_no].marks = marks
            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    def delete_student(self):
        roll_no = int(input("Enter Roll No to Delete: "))
        if roll_no in self.students:
            del self.students[roll_no]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    def display_all(self):
        if not self.students:
            print("No Records Found!")
        else:
            for student in self.students.values():
                student.display()
                print("-" * 20)


manager = StudentManager()

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        manager.add_student()
    elif choice == 2:
        manager.search_student()
    elif choice == 3:
        manager.update_student()
    elif choice == 4:
        manager.delete_student()
    elif choice == 5:
        manager.display_all()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")