
from abc import ABC, abstractclassmethod

#univercfity
class Univercity(ABC):
    def __init__(self):
        self.students = []
        self.employees = []
       
    @abstractclassmethod
    def show_info(self):
        pass
   

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                break

    def edit_student(self, student_id, first_name=None, last_name=None, age=None, score=None):
        for student in self.students:
            if student.student_id == student_id:
                if first_name:
                    student.first_name = first_name
                if last_name:
                    student.last_name = last_name
                if age:
                    student.age = age
                if score:
                    student.score = score
                break

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_students(self):
        for student in self.students:
            student.all_info_display()
            print()

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                break

    def edit_employee(self, employee_id, name=None, last_name=None, age=None, salary=None):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                if name:
                    employee.name = name
                if last_name:
                    employee.last_name = last_name
                if age:
                    employee.age = age
                if salary:
                    employee.salary = salary
                break

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None


#student
class Student(Univercity):
    def __init__(self, first_name, last_name, age, student_id, score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.score = score

    def all_info_display(self):
        return f"ID : {self.student_id} ,name : {self.first_name} , last name : {self.last_name} , age :{self.age} , score : {self.score}"

    def info_display(self):
        print ("first name :" , self.first_name)
        print("last name :" , self.last_name)
        print("Age:", self.age)

       
    def show_info(self):
        print (f"{self.name} is a Student")
       
       
#employee
class Employee(Univercity):
    def __init__(self, name, last_name, age, employee_id, salary):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.employee_id = employee_id
        self.salary = salary

    def info_display(self):
        print("Name:", self.name)
        print("last_name:", self.last_name)
        print("Age:", self.age)

    def all_info_display(self):
        return f"ID : {self.student_id} ,name : {self.name} , last name : {self.last_name} , age :{self.age} , employee : {self.employee_id} , salary : {self.salary}"

    def show_info(self):
        print (f"{self.name} is a employees")



if __name__ == "__main__":
    s1 = Student("a" ,"b" ,18 ,"123" ,17)
    print (vars(s1))
    e1 = Employee("k" ,"c" ,19 ,"827" ,30)
    print (vars(e1))
    s1.edit_student(student_id = "123" , age= 60)
    print(s1)
    e1.show_info()
    print(e1)


