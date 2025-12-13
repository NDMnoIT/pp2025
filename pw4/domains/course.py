"""Course class for managing course information."""


class Course:
    """Represents a course with ID, name, and credit hours."""
    
    def __init__(self, cid, name, credits=3):
        """Initialize a course with ID, name, and credits.
        
        Args:
            cid (str): Course ID
            name (str): Course name
            credits (float): Credit hours (default: 3)
        """
        self.id, self.name, self.credits = cid, name, credits
    
    @staticmethod
    def input():
        """Get course information from user input.
        
        Returns:
            Course: A new Course object with user-provided information
        """
        cid = input("Course ID: ")
        name = input("Course name: ")
        credits = float(input("Credits: "))
        return Course(cid, name, credits)
    
    def __str__(self):
        """Return string representation of the course.
        
        Returns:
            str: Formatted course information with credits
        """
        return f"{self.id} - {self.name} ({self.credits} credits)"
