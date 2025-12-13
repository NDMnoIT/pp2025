"""Input module for handling user input operations."""

from domains.student import Student
from domains.course import Course


def input_students(manager, count):
    """Input multiple students into the manager.
    
    Args:
        manager (Manager): The manager instance
        count (int): Number of students to input
    """
    for _ in range(count):
        s = Student.input()
        manager.students[s.id] = s


def input_course(manager):
    """Input a single course into the manager.
    
    Args:
        manager (Manager): The manager instance
    """
    c = Course.input()
    manager.courses[c.id] = c


def input_marks(manager):
    """Input marks for a course.
    
    Args:
        manager (Manager): The manager instance
    """
    cid = input("Course ID: ")
    if cid in manager.courses:
        manager.marks.input(cid, manager.students)
    else:
        print("Course not found.")


def get_student_id():
    """Get a student ID from user input.
    
    Returns:
        str: The student ID
    """
    return input("Student ID: ")


def get_course_id():
    """Get a course ID from user input.
    
    Returns:
        str: The course ID
    """
    return input("Course ID: ")


def get_num_students():
    """Get the number of students from user input.
    
    Returns:
        int: The number of students
    """
    return int(input("How many? "))


def get_menu_choice():
    """Get the user's menu choice.
    
    Returns:
        str: The menu choice
    """
    print("\n1.Input Students  2.Input Courses  3.Input Marks")
    print("4.List Students  5.List Courses   6.Show Marks  7.Show GPA")
    print("8.Sort by GPA    0.Exit")
    return input("Choice: ")
