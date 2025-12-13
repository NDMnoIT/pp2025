"""Student class for managing student information."""


class Student:
    """Represents a student with ID, name, and date of birth."""
    
    def __init__(self, sid, name, dob):
        """Initialize a student with ID, name, and date of birth.
        
        Args:
            sid (str): Student ID
            name (str): Student name
            dob (str): Date of birth
        """
        self.id, self.name, self.dob = sid, name, dob
    
    @staticmethod
    def input():
        """Get student information from user input.
        
        Returns:
            Student: A new Student object with user-provided information
        """
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        return Student(sid, name, dob)
    
    def __str__(self):
        """Return string representation of the student.
        
        Returns:
            str: Formatted student information
        """
        return f"{self.id} - {self.name} ({self.dob})"
