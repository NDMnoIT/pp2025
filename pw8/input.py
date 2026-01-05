"""Input module for handling user input operations."""

from domains.student import Student
from domains.course import Course


def _save_students(manager):
    """Internal function to save all students to students.txt."""
    with open("students.txt", "w") as f:
        for student in manager.students.values():
            f.write(f"{student.to_csv()}\n")


def input_students(manager, count):
    """Input multiple students into the manager and save to file."""
    for _ in range(count):
        s = Student.input()
        manager.students[s.id] = s
    
    _save_students(manager)


def _save_courses(manager):
    """Internal function to save all courses to courses.txt."""
    with open("courses.txt", "w") as f:
        for course in manager.courses.values():
            f.write(f"{course.to_csv()}\n")


def input_course(manager):
    """Input a single course into the manager and save to file."""
    c = Course.input()
    manager.courses[c.id] = c
    
    _save_courses(manager)


def input_marks(manager):
    """Input marks for a course and save to file."""
    cid = input("Course ID: ")
    if cid in manager.courses:
        manager.marks.input(cid, manager.students)
        
        manager.marks.save_to_file("marks.txt")
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
