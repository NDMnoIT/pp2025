"""Manager class for coordinating student, course, and mark operations."""

import math
import pickle 
import os 
from .student import Student
from .course import Course
from .mark import Mark


class Manager:
    """Manages students, courses, marks, and GPA calculations."""
    
    def __init__(self):
        """Initialize the manager with empty collections."""
        self.students = {}
        self.courses = {}
        self.marks = Mark()
    
    def save_data(self, filename="students.dat"):
        """Compresses all data into students.dat using pickle."""
        try:

            with open(filename, 'wb') as f:

                pickle.dump({
                    'students': self.students,
                    'courses': self.courses,
                    'marks_data': self.marks.data  
                }, f)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename="students.dat"):
        """Checks if students.dat exists, decompresses, and loads data."""
        if not os.path.exists(filename):
            print(f"No previous data found in {filename}.")
            return
        
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
                
                self.students = data.get('students', {})
                self.courses = data.get('courses', {})
                self.marks.data = data.get('marks_data', {})
                self.marks.rebuild_arrays() 

            print(f"Data successfully loaded from {filename}.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def calculate_gpa(self, student_id):
        """Calculate GPA for a given student using weighted sum.
        
        Args:
            student_id (str): The student ID
            
        Returns:
            float: The calculated GPA rounded down to 1 decimal place
        """
        if student_id not in self.students:
            return 0.0
        
        total_credits = 0
        weighted_sum = 0
        
        for course_id, course in self.courses.items():
            mark = self.marks.get_mark(course_id, student_id)
            if mark is not None:
                weighted_sum += mark * course.credits
                total_credits += course.credits
        
        if total_credits == 0:
            return 0.0
        
        gpa = weighted_sum / total_credits
        gpa = math.floor(gpa * 10) / 10
        return gpa
    
    def sort_students_by_gpa(self):
        """Sort students by GPA in descending order.
        
        Returns:
            list: List of tuples (Student, GPA) sorted by GPA descending
        """
        student_list = []
        for sid, student in self.students.items():
            gpa = self.calculate_gpa(sid)
            student_list.append((student, gpa))
        
        student_list.sort(key=lambda x: x[1], reverse=True)
        return student_list
    
    def get_students(self):
        """Get all students.
        
        Returns:
            dict: Dictionary of all students
        """
        return self.students
    
    def get_courses(self):
        """Get all courses.
        
        Returns:
            dict: Dictionary of all courses
        """
        return self.courses
    
    def get_marks(self):
        """Get the marks object.
        
        Returns:
            Mark: The Mark instance
        """
        return self.marks