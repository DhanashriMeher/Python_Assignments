#Vowel or Consonant Check.
#Accept a single character from the user and check if it is a vowel(a,e,i,o,u).If not
#print It's consonant.

def CheckVowel(char):
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        print( char +" is Vowel")
    else:
        print(char +" is consonant")


def main():
    Result = str(input("Enter a character : "))
    CheckVowel(Result)

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_2.py
#Enter a character : e
#e is Vowel

#C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_2.py
#Enter a character : r
#r is consonant        