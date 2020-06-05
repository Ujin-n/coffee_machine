class Student:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + birth_year


fname = input()
lname = input()
byear = input()

student = Student(fname, lname, byear)

print(student.id)
