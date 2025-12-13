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
    def __init__(self, cid, name):
        self.id, self.name = cid, name
    @staticmethod
    def input():
        cid = input("Course ID: ")
        name = input("Course name: ")
        return Course(cid, name)
    def __str__(self):
        return f"{self.id} - {self.name}"
class Mark:
    def __init__(self):
        self.data = {}
    def input(self, course_id, students):
        if course_id not in self.data:
            self.data[course_id] = {}
        for sid in students:
            m = float(input(f"Mark for {sid}: "))
            self.data[course_id][sid] = m
    def list(self, course_id):
        if course_id not in self.data:
            print("No marks.")
            return
        for sid, m in self.data[course_id].items():
            print(f"{sid}: {m}")
class Manager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = Mark()
    def run(self):
        while True:
            print("\n1.Input Students  2.Input Courses  3.Input Marks")
            print("4.List Students  5.List Courses   6.Show Marks  0.Exit")
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
            elif c == '0':
                break
if __name__ == "__main__":
    Manager().run()