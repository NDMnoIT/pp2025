students = {} # {id: {'name': name, 'DoB': dob}}
courses = {}  # {id: name}
marks = {}    # {course_id: {student_id: mark}}

def input_num_students():
    """Input and return the number of students."""
    try:
        n = int(input("Enter number of students: "))
        return n
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def input_student_info(n):
    """Input student info (ID, name, DoB) for n students."""
    for i in range(n):
        print(f"\n--- Input Student {i+1} ---")
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        students[student_id] = {'name': name, 'DoB': dob}
        print(f"Student {student_id} added.")

def list_courses():
    """List all courses."""
    print("\n--- Available Courses ---")
    if not courses:
        print("No courses available.")
        return
    for c_id, name in courses.items():
        print(f"ID: {c_id}, Name: {name}")

def main():
    """Main function to run the program loop."""
    while True:
        print("\n==============================")
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Input Student Information")
        print("2. Input Course Information")
        print("3. Input Marks for a Course")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Student Marks for a Course")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n = input_num_students()
            if n > 0:
                input_student_info(n)
        # ... (Add logic for other choices)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()