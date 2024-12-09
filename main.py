import pickle
class Course_grade:
    def __init__(self):
        self.course = input("Enter the course name: ")
        self.num_students = int(input(f"Enter the number of students for {self.course} (at least 5): "))
        self.students = []
        for _ in range(self.num_students):
            name = input("Enter student name: ")
            ID = input("Enter student ID: ")
            grade = int(input("Enter student grade: "))
            self.students.append({"name": name, "ID": ID, "grade": grade})

    def final_grade(self, grade):
        if grade >= 94:
            return "A"
        elif grade >= 90:
            return "A-"
        elif grade >= 87:
            return "B+"
        elif grade >= 83:
            return "B"
        elif grade >= 80:
            return "B-"
        elif grade >= 77:
            return "C+"
        elif grade >= 73:
            return "C"
        elif grade >= 70:
            return "C-"
        elif grade >= 67:
            return "D+"
        elif grade >= 65:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"\nCourse: {self.course}")
        print("Students:")
        for student in self.students:
            print(
                f"  Name: {student['name']}, ID: {student['ID']}, Grade: {student['grade']}, Final Grade: {self.final_grade(student['grade'])}")
        print()


courses = []
for i in range(4):
    print(f"\nCreating Course {i + 1}:")
    course = Course_grade()
    courses.append(course)

with open("grades_info.dat", "ab") as f:
    for course in courses:
        pickle.dump(course, f)

print("\nReading objects from file:\n")
with open("grades_info.dat", "rb") as f:
    while True:
        try:
            course = pickle.load(f)
            course.display()
        except EOFError:
            break
