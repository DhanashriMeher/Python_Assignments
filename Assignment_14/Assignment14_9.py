#Create a class product with attributes name and price.Implement __eq__ method to compare two product if they
#are equal in price.

class Product:

    def __init__(self):
        self.name = input("Enter Product : ")
        self.price = float(input("Enter Price of Product : "))

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False
     

def main():
    obj = Product()
    print("\nName of Product : " +obj.name)
    print("Price of product : " ,obj.price)

    obj1 = Product()
    print("\nName of Second Product : " +obj1.name)
    print("Price of Second product : " ,obj1.price)

    if (obj.price == obj1.price):
        print("\nPrices are equal")
    else:
        print("\nPrices are not equal")    

if __name__ == "__main__":
    main()



        