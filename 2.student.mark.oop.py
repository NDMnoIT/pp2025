class Student:
    """Represents a student with proper encapsulation."""
    
    def __init__(self, student_id, name, dob):
        
        self._student_id = student_id
        self._name = name
        self._dob = dob

        self.marks = {}

    
    def get_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def add_mark(self, course_id, mark):
        """Method to add or update a mark for a course."""
        if 0 <= mark <= 20:
            self.marks[course_id] = mark
        else:
            print(f"Error: Invalid mark {mark} for {self._name}.")

    def list(self): 
        """Method for listing student info. Demonstrates polymorphism with Course.list()"""
        print(f"Student ID: {self._student_id} | Name: {self._name} | DoB: {self._dob}")

    def __str__(self):
        return f"Student(ID: {self._student_id}, Name: {self._name})"

class Course:
    """Represents a course with proper encapsulation."""
    
    def __init__(self, course_id, name):
        self._course_id = course_id
        self._name = name

    def get_id(self):
        return self._course_id

    def get_name(self):
        return self._name

    def list(self):
        """Method for listing course info. Demonstrates polymorphism with Student.list()"""
        print(f"Course ID: {self._course_id} | Name: {self._name}")

    def __str__(self):
        return f"Course(ID: {self._course_id}, Name: {self._name})"


class MarkManagementSystem:
    """Manages collections of students and courses."""
    
    def __init__(self):

        self.__students = {}
        self.__courses = {}

    def input(self, entity_type):
        """A polymorphic method to input either students or courses."""
        
        if entity_type.lower() == 'student':
            print("\n--- Input New Student ---")
            student_id = input("Enter student ID: ")
            if student_id in self.__students:
                print("Error: Student ID already exists.")
                return
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (DoB): ")
            
            new_student = Student(student_id, name, dob)
            self.__students[student_id] = new_student
            print(f"Student {student_id} ('{name}') added.")

        elif entity_type.lower() == 'course':
            print("\n--- Input New Course ---")
            course_id = input("Enter course ID: ")
            if course_id in self.__courses:
                print("Error: Course ID already exists.")
                return
            name = input("Enter course name: ")
            
            new_course = Course(course_id, name)
            self.__courses[course_id] = new_course
            print(f"Course {course_id} ('{name}') added.")
            
        else:
            print("Invalid entity type for input.")
            
    def list(self, entity_type):
        """A polymorphic method to list either students or courses."""
        
        if entity_type.lower() == 'student':
            print("\n--- List of Students ---")
            if not self.__students:
                print("No students have been added.")
                return
            for student in self.__students.values():
                student.list() 

        elif entity_type.lower() == 'course':
            print("\n--- List of Courses ---")
            if not self.__courses:
                print("No courses have been added.")
                return
            for course in self.__courses.values():
                course.list()
                
        else:
            print("Invalid entity type for list.")

    def input_marks_for_course(self):
        """Selects a course and inputs marks for students."""
        if not self.__courses or not self.__students:
            print("\nCannot input marks. Ensure students and courses have been added.")
            return

        self.list('course')
        selected_course_id = input("Enter the ID of the course to input marks for: ")
        
        if selected_course_id not in self.__courses:
            print(f"Error: Course ID '{selected_course_id}' not found.")
            return

        course_name = self.__courses[selected_course_id].get_name()
        print(f"\nInputting marks for course: {course_name}")
        
        for student_id, student in self.__students.items():
            while True:
                try:
                    mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student_id}): "))
                    if 0 <= mark <= 20: 
                        break
                    else:
                        print("Mark must be between 0 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            student.add_mark(selected_course_id, mark)
            print(f"Mark {mark} recorded for {student.get_name()}.")

    def show_student_marks_for_given_course(self):
        """Shows all student marks for a selected course."""
        if not self.__courses:
            print("\nNo courses available.")
            return

        self.list('course')
        course_id = input("Enter the ID of the course to view marks for: ")
        
        if course_id not in self.__courses:
            print(f"Error: Course ID '{course_id}' not found.")
            return
        
        course_name = self.__courses[course_id].get_name()
        print(f"\n--- Marks for Course: {course_name} ---")
        
        found_marks = False
        for student in self.__students.values():
            if course_id in student.marks:
                print(f"Student: {student.get_name()} (ID: {student.get_id()}) | Mark: {student.marks[course_id]}")
                found_marks = True
                
        if not found_marks:
            print(f"No marks recorded yet for the course '{course_name}'.")

def main_practical_work_2():
    """Main function to run the OOP student mark management system."""
    
    manager = MarkManagementSystem()

    num_students = int(input("Input number of students in the class: "))
    for _ in range(num_students):
        manager.input('student')

    num_courses = int(input("\nInput number of courses: "))
    for _ in range(num_courses):
        manager.input('course')  

    manager.input_marks_for_course()
    
    manager.list('student') 
    manager.list('course')
    manager.show_student_marks_for_given_course()
    
    print("\nPractical Work 2 (OOP'ed) completed.")
    print("Don't forget to push your work to the corresponding forked Github repository.")
