class Person:
    """Base class representing a general person in the system."""
    
    def __init__(self, name: str, email: str, person_id: str):
        # Public attribute
        self.name = name
        
        # Encapsulated (protected) attributes
        self._email = email
        self._person_id = person_id

    @property
    def email(self) -> str:
        """Getter for email."""
        return self._email

    @email.setter
    def email(self, new_email: str):
        """Setter with basic email validation."""
        if "@" not in new_email:
            raise ValueError("Invalid email address provided.")
        self._email = new_email

    @property
    def person_id(self) -> str:
        """Getter for person_id (read-only attribute)."""
        return self._person_id

    def get_role(self) -> str:
        """Method meant to be overridden by child classes (Polymorphism)."""
        return "Person"

    def __str__(self) -> str:
        """String representation of the object."""
        return f"[{self.get_role()}] {self.name} (ID: {self._person_id})"