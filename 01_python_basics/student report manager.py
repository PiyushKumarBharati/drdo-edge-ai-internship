class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for student in self.students:
                print(student)

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                print("Found:", student)
                return
        print("Student not found.")

    def delete_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"Student {name} deleted successfully!")
                return
        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            manager.add_student(name, grade)
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            name = input("Enter student name to search: ")
            manager.search_student(name)
        elif choice == "4":
            name = input("Enter student name to delete: ")
            manager.delete_student(name)
        elif choice == "5":
            print("Exiting Student Record Manager...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
