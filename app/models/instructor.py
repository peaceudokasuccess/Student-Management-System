from app.models.person import Person

class Instructor(Person):
    """Instructor class inheriting from Person."""
    
    def __init__(self, name: str, email: str, employee_id: str, department: str):
        super().__init__(name, email, employee_id)
        self.department = department

    def get_role(self) -> str:
        """Override base method (Polymorphism)."""
        return "Instructor"

    def __str__(self) -> str:
        return f"[{self.get_role()}] Prof. {self.name} | Dept: {self.department}"