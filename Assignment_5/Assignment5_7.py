#Area and Perimeter of Rectangle
#Accept the length and width of a rectangle.Calculate and Display the area and Perimeter.

def AreaOfRectangle(length,width):
    Area = (length * width)
    return Area

def PerimeterOfRect(length,width):
    Perimeter = 2*(length + width)
    return Perimeter

def main():
    len = float(input("Enter length : "))
    width = float(input("Enter width : "))
    
    print("Area Of Rectangle : " ,AreaOfRectangle(len,width))
    print("Perimeter of Rectangle : ",PerimeterOfRect(len,width))

if __name__ == "__main__" :
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_7.py
#Enter length : 5
#Enter width : 3
#Area Of Rectangle :  15.0
#Perimeter of Rectangle :  16.0    


