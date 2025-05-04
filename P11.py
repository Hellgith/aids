class Student:
    def __init__(self, roll, name, division, address):
        self.roll = roll
        self.name = name
        self.division = division
        self.address = address

    def display(self):
        print(f"Roll Number: {self.roll}, Name: {self.name}, Division: {self.division}, Address: {self.address}")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, roll, name, division, address):
        if roll in self.students:
            print("Student with this roll number already exists.")
        else:
            self.students[roll] = Student(roll, name, division, address)
            print("Student added successfully.")

    def delete_student(self, roll):
        if roll in self.students:
            del self.students[roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def display_student(self, roll):
        if roll in self.students:
            self.students[roll].display()
        else:
            print("Student not found.")

    def display_all(self):
        if self.students:
            for student in self.students.values():
                student.display()
        else:
            print("No records available.")

def main():
    manager = StudentManager()
    while True:
        print("\n1. Add\n2. Delete\n3. Display One\n4. Display All\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            manager.add_student(input("Roll: "), input("Name: "), input("Div: "), input("Address: "))
        elif choice == '2':
            manager.delete_student(input("Enter roll to delete: "))
        elif choice == '3':
            manager.display_student(input("Enter roll to display: "))
        elif choice == '4':
            manager.display_all()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
