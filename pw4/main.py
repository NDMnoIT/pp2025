"""Main script for the Student Management System."""

from domains import Manager
import input as input_module
import output as output_module


def main():
    """Main entry point for the student management system."""
    manager = Manager()
    
    while True:
        choice = input_module.get_menu_choice()
        
        if choice == '1':
            try:
                count = input_module.get_num_students()
                input_module.input_students(manager, count)
            except ValueError:
                output_module.display_error("Invalid input. Please enter a number.")
        
        elif choice == '2':
            try:
                input_module.input_course(manager)
            except ValueError:
                output_module.display_error("Invalid input. Please check your entries.")
        
        elif choice == '3':
            input_module.input_marks(manager)
        
        elif choice == '4':
            output_module.display_students(manager.students)
        
        elif choice == '5':
            output_module.display_courses(manager.courses)
        
        elif choice == '6':
            cid = input_module.get_course_id()
            output_module.display_marks(manager.marks, cid)
        
        elif choice == '7':
            sid = input_module.get_student_id()
            gpa = manager.calculate_gpa(sid)
            output_module.display_gpa(sid, gpa)
        
        elif choice == '8':
            sorted_students = manager.sort_students_by_gpa()
            output_module.display_students_sorted_by_gpa(sorted_students)
        
        elif choice == '0':
            print("Goodbye!")
            break
        
        else:
            output_module.display_error("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
