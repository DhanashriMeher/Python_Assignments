#Create a base class Person with name and age. Derive a class Teacher with subject and salary.Use Super() to call 
#base class constructor and print both.

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : ",self.name ,"\nage : ",self.age)

class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def Display(self):
        super().display()
        print("Teacher Subjects : ",self.subject)
        print("Salary of Teacher : ",self.salary)

def main():
    obj = Teacher("Ajay",35,"Operating System",35000)
    obj.Display()

if __name__ =="__main__":
    main()            

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_7.py
#Name :  Ajay
#age :  35
#Teacher Subjects :  Operating System
#Salary of Teacher :  35000
