#Create a class Employee with attributes name,emp_id and salary. Create objects of this class and print their details
#using a method.

class Employee:

    def __init__(self,Name,Emp_id,Salary):
        self.Name = Name
        self.Emp_id = Emp_id
        self.Salary = Salary

    def display(self):
        print("Name of Employee : ",self.Name)
        print("Employee Id :",self.Emp_id)
        print("Salary of Employee : ",self.Salary)

def main():
    obj1 = Employee('Rohit',101,50000)
    obj1.display()

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_1.py
#Name of Employee :  Rohit
#Employee Id : 101
#Salary of Employee :  50000
    