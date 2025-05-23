#Celsius to Fahrenheit Converter
#Accept temperature in celsius and convert it to Fahrenheit using the formula:
#F =(C * 9/5)+32


def main():
    Celsius = float(input(" Enter temperature in Celsius : "))
    Result = (Celsius * 1.8)+32

    print("Temperature in Fahrenheit : ",Result ,"F")

if __name__ == "__main__" :
    main()

#C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_6.py
#Enter temperature in Celsius : 25
#Temperature in Fahrenheit :  77.0 F

