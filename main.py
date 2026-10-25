from app.models.student import Student
from app.models.instructor import Instructor

if __name__ == "__main__":
    student1 = Student("Alice Smith", "alice@university.edu", "S1001", "Computer Science")
    instructor1 = Instructor("Dr. Bob", "bob@university.edu", "I5001", "Mathematics")

    student1.enroll("CS101")
    student1.enroll("MATH201")

    print(student1)
    print(instructor1)