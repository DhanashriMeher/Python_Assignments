#Write a function that accepts a string and checks whether it is a palindrome 

def isPalindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("not Palindrome")
  

def main():
    string = (input("Enter a string : "))
    isPalindrome(string)

if __name__ == "__main__":
    main()
