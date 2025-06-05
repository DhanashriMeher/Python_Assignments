#Demonstrate public.private,protected access modifiers using class Employee with attributes : _salary,_department,name

class Employee:

    def __init__(self, name, department, salary):
        self.name = name              # public
        self._department = department  # protected
        self.__salary = salary        # private
  
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")
         

def main():
    emp = Employee("Pallavi", "IT", 50000)

    print("Public name:", emp.name)  
    print("Protected _department:", emp._department)
    
    print("Salary:", emp.get_salary())

    emp.set_salary(75000)
    emp.display()

if __name__ == "__main__":
    main()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_10.py
#Public name: Pallavi
#Protected _department: IT
#Salary: 50000
#Name: Pallavi
#Department: IT
#Salary: 75000