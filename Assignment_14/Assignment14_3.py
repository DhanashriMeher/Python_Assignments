#Create a class Book with private attribute __price. Add Methods to get and set the price.Show Encapsulation.

class Book:

    def __init__(self,Price):
        self.__Price = Price

    def getPrice(self):
        return self.__Price 

    def setPrice(self,newPrice):
        if(newPrice > 0):
            self.__Price = newPrice
        else:
            print("Invalid Price")

def main():
    obj = Book(100)

    print("Original Price of Book",obj.getPrice())

    obj.setPrice(200) 
    print("Updated Price : ",obj.getPrice())           

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_14>python Assignment14_3.py
#Original Price of Book 100
#Updated Price :  200

        
