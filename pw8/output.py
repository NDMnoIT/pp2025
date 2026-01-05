"""Output module for displaying information to the user."""


def display_students(students):
    """Display all students.
    
    Args:
        students (dict): Dictionary of students
    """
    if not students:
        print("No students.")
    else:
        for student in students.values():
            print(student)


def display_courses(courses):
    """Display all courses.
    
    Args:
        courses (dict): Dictionary of courses
    """
    if not courses:
        print("No courses.")
    else:
        for course in courses.values():
            print(course)


def display_marks(marks, course_id):
    """Display marks for a course.
    
    Args:
        marks (Mark): The Mark instance
        course_id (str): The course ID
    """
    marks.list(course_id)


def display_gpa(student_id, gpa):
    """Display GPA for a student.
    
    Args:
        student_id (str): The student ID
        gpa (float): The calculated GPA
    """
    print(f"GPA for {student_id}: {gpa}")


def display_students_sorted_by_gpa(sorted_list):
    """Display students sorted by GPA.
    
    Args:
        sorted_list (list): List of tuples (Student, GPA) sorted by GPA
    """
    print("\nStudents sorted by GPA (Descending):")
    if not sorted_list:
        print("No students.")
    else:
        for student, gpa in sorted_list:
            print(f"{student} - GPA: {gpa}")


def display_error(message):
    """Display an error message.
    
    Args:
        message (str): The error message
    """
    print(f"Error: {message}")
