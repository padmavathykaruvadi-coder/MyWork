# 1) Define a class to model a student
class Student:
    # 2) Constructor: runs when you create a Student()
    def __init__(self, name: str, grade: str, department: str):
        # 3) Save the data on the object (self points to the current object)
        self.name = name
        self.grade = grade
        self.department = department

    # 4) Method to print all details of the student
    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}")

    # 5) Method to update the student's grade
    def update_grade(self, new_grade: str):
        self.grade = new_grade  # change the grade stored on this object

# 6) Main section: only runs when this file is executed directly
if __name__ == "__main__":
    # 7) Create at least three Student objects with different details
    s1 = Student("Aisha", "A", "Computer Science")
    s2 = Student("Rohan", "B+", "Mechanical Engineering")
    s3 = Student("Meera", "A-", "Physics")

    # 8) Manage multiple students using a list
    students = [s1, s2, s3]

    # 9) Print each student's information (initial state)
    print("--- Student Records (Initial) ---")
    for s in students:
        s.print_info()

    # 10) Update the grade of one student and print updated details
    print("\n--- Updating Rohan's grade to A ---")
    s2.update_grade("A")
    s2.print_info()

    # 11) Display all records again to show the list still reflects the change
    print("\n--- Student Records (After Update) ---")
    for s in students:
        s.print_info()
