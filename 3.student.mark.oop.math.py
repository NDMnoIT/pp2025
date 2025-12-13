import math
import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.id, self.name, self.dob = sid, name, dob
    @staticmethod
    def input():
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        return Student(sid, name, dob)
    def __str__(self):
        return f"{self.id} - {self.name} ({self.dob})"

class Course:
    def __init__(self, cid, name, credits=3):
        self.id, self.name, self.credits = cid, name, credits
    @staticmethod
    def input():
        cid = input("Course ID: ")
        name = input("Course name: ")
        credits = float(input("Credits: "))
        return Course(cid, name, credits)
    def __str__(self):
        return f"{self.id} - {self.name} ({self.credits} credits)"

class Mark:
    def __init__(self):
        self.data = {}
    def input(self, course_id, students):
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
        if course_id not in self.data:
            print("No marks.")
            return
        for sid, m in self.data[course_id].items():
            if sid != '_array':
                print(f"{sid}: {m}")
    def get_mark(self, course_id, student_id):
        if course_id in self.data and student_id in self.data[course_id]:
            return self.data[course_id][student_id]
        return None

class Manager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = Mark()
    
    def calculate_gpa(self, student_id):
        """Calculate GPA for a given student using weighted sum"""
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
        """Sort students by GPA in descending order"""
        student_list = []
        for sid, student in self.students.items():
            gpa = self.calculate_gpa(sid)
            student_list.append((student, gpa))
        
        student_list.sort(key=lambda x: x[1], reverse=True)
        return student_list
    
    def run(self):
        while True:
            print("\n1.Input Students  2.Input Courses  3.Input Marks")
            print("4.List Students  5.List Courses   6.Show Marks  7.Show GPA")
            print("8.Sort by GPA    0.Exit")
            c = input("Choice: ")
            if c == '1':
                for _ in range(int(input("How many? "))):
                    s = Student.input()
                    self.students[s.id] = s
            elif c == '2':
                c = Course.input()
                self.courses[c.id] = c
            elif c == '3':
                cid = input("Course ID: ")
                if cid in self.courses:
                    self.marks.input(cid, self.students)
            elif c == '4':
                [print(s) for s in self.students.values()]
            elif c == '5':
                [print(c) for c in self.courses.values()]
            elif c == '6':
                cid = input("Course ID: ")
                self.marks.list(cid)
            elif c == '7':
                sid = input("Student ID: ")
                gpa = self.calculate_gpa(sid)
                print(f"GPA for {sid}: {gpa}")
            elif c == '8':
                print("\nStudents sorted by GPA (Descending):")
                for student, gpa in self.sort_students_by_gpa():
                    print(f"{student} - GPA: {gpa}")
            elif c == '0':
                break

if __name__ == "__main__":
    Manager().run()