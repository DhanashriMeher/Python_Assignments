#Write a program which contains one class named as BookStore.
#BookStore class contains two instance variable as Name, Author.
#That class contains one class variable as NoOfBooks which is initialise to 0.
#There is one instance methods of class as Display which displays name,Author and number of books.
#Initialise instance variable to init method by accepting the values from user as name and author.
#Inside init method increment value of NoOfBooks by one.
#After creating class Create the two objects of BookStore class a
#obj1 = BookStore("Linux system programming","Robert Love")
#obj1.Display()

class BookStore():

    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):
        print("Name of Book : ",self.Name)
        print("Author Name of Book :",self.Author)
        print("Books : ",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")    
    obj1.Display()

    print()

    obj2 =BookStore("C Programming", "Dennis Rotchie")
    obj2.Display()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_13>python Assignment13_1.py
#Name of Book :  Linux System Programming
#Author Name of Book : Robert Love
#Books :  1

#Name of Book :  C Programming
#Author Name of Book : Dennis Rotchie
#Books :  2

