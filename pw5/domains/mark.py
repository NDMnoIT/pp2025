"""Mark class for managing student marks."""

import math
import numpy as np


class Mark:
    """Manages marks for students across courses with floor rounding."""
    
    def __init__(self):
        """Initialize the Mark storage system."""
        self.data = {}
    
    def input(self, course_id, students):
        """Input marks for all students in a course.
        
        Args:
            course_id (str): The course ID
            students (dict): Dictionary of student IDs
        """
        if course_id not in self.data:
            self.data[course_id] = {}
        
        marks_list = []
        for sid in students:
            m = float(input(f"Mark for {sid}: "))

            m = math.floor(m * 10) / 10
            marks_list.append(m)
            self.data[course_id][sid] = m
        

        self.data[course_id]['_array'] = np.array(marks_list)
    
    def list(self, course_id):
        """Display all marks for a course.
        
        Args:
            course_id (str): The course ID
        """
        if course_id not in self.data:
            print("No marks.")
            return
        
        for sid, m in self.data[course_id].items():
            if sid != '_array':
                print(f"{sid}: {m}")

    def rebuild_arrays(self):
        """Rebuilds the numpy array storage for each course after data load."""
        for course_id, course_data in self.data.items():
            marks_list = [mark for sid, mark in course_data.items() if sid != '_array']
            self.data[course_id]['_array'] = np.array(marks_list)

    def save_to_file(self, filename="marks.txt"):
        """Save all marks (course_id, student_id, mark) to a text file."""
        with open(filename, 'w') as f:
            for course_id, course_data in self.data.items():
                for student_id, mark in course_data.items():
                    if student_id != '_array':
                        f.write(f"{course_id},{student_id},{mark}\n")
    
    def get_mark(self, course_id, student_id):
        """Get a specific student's mark in a course.
        
        Args:
            course_id (str): The course ID
            student_id (str): The student ID
            
        Returns:
            float: The mark, or None if not found
        """
        if course_id in self.data and student_id in self.data[course_id]:
            return self.data[course_id][student_id]
        return None
