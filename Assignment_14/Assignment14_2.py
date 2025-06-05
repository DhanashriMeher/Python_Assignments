#Write class Rectangle with length and width.Add a method to compute area and perimeter.
#Area : 50 ,Perimeter : 30

class Rectangle:

    def __init__(self):
        self.Length = int(input("Enter Length :"))
        self.Width = int(input("Enter Width:"))

    def Area(self):
        return self.Length * self.Width

    def Perimeter(self):
        return 2*(self.Length + self.Width)   

def main():
    obj=Rectangle()
    obj.Area()
    obj.Perimeter()
    print("Area:", obj.Area())           
    print("Perimeter:", obj.Perimeter()) 

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_2.py
#Enter Length : 10
#Enter Width:5
#Area: 50
#Perimeter: 30
