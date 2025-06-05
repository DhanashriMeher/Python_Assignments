#Create a class Student with name,roll_no and a class variable school_name.Print student details ans school name
#Change the school name using class name.

class Student:

    school_name = "GRP Sabnis"

    def __init__(self,name,Roll_no):
        self.name = name
        self.Roll_no = Roll_no

    def display_details(self):
        print("Name: "+self.name)
        print("Roll No: " ,self.Roll_no)
        print("School Name: " +Student.school_name)

def main():
    obj = Student("Savita" , 101)
    obj.display_details()

    obj1 =Student("Sarika",102)
    obj1.display_details()

    Student.school_name = "Modern"
    print("\nChange School_name :" +Student.school_name)

    obj.display_details()
    obj1.display_details()


if __name__ == "__main__":
    main()        

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_4.py
#Name: Savita
#Roll No:  101
#School Name: GRP Sabnis
#Name: Sarika
#Roll No:  102
#School Name: GRP Sabnis

#Change School_name :Modern
#Name: Savita
#Roll No:  101
#School Name: Modern
#Name: Sarika
#Roll No:  102
#School Name: Modern        