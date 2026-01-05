"""Manager class for coordinating student, course, and mark operations.

This version saves and loads data using pickle compressed with gzip
and performs saves in a background thread to avoid blocking the main UI.
"""

import math
import pickle
import os
import gzip
import threading
import tempfile
import shutil
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
    
    def _background_save(self, filename, data):
        tmp = None
        try:
            dirn = os.path.dirname(os.path.abspath(filename)) or '.'
            fd, tmp = tempfile.mkstemp(dir=dirn, prefix='.tmp_save_', suffix='.gz')
            os.close(fd)

            with gzip.open(tmp, 'wb') as f:
                pickle.dump(data, f)

            shutil.move(tmp, filename)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data in background: {e}")
            try:
                if tmp and os.path.exists(tmp):
                    os.remove(tmp)
            except Exception:
                pass

    def save_data(self, filename="students.dat.gz"):
        """Start a background thread to gzip-compress and pickle current data.

        The save is asynchronous; the thread is started as a daemon so it won't
        prevent program exit (but that means a rapid exit may stop the save).
        """
        data = {
            'students': self.students,
            'courses': self.courses,
            'marks_data': self.marks.data
        }

        thread = threading.Thread(target=self._background_save, args=(filename, data), daemon=True)
        thread.start()
        print(f"Save started in background to {filename}")

    def load_data(self, filename="students.dat.gz"):
        """Load compressed pickled data if the file exists."""
        if not os.path.exists(filename):
            print(f"No previous data found in {filename}.")
            return
        
        try:
            with gzip.open(filename, 'rb') as f:
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
