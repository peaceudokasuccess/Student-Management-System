from app.models.person import Person

class Student(Person):
    """Student class inheriting from Person."""
    
    def __init__(self, name: str, email: str, student_id: str, major: str):
        # Initialize base Person attributes
        super().__init__(name, email, student_id)
        self.major = major
        self.courses = []  # List to store enrolled course objects

    def get_role(self) -> str:
        """Override base method (Polymorphism)."""
        return "Student"

    def enroll(self, course_code: str):
        """Add a course code to enrolled courses."""
        if course_code not in self.courses:
            self.courses.append(course_code)

    def __str__(self) -> str:
        return f"[{self.get_role()}] {self.name} | Major: {self.major} | Courses: {len(self.courses)}"