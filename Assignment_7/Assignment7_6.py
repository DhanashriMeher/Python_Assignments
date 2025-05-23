#Write a function that accepts a list of integer and returns a list of prime numbers using filter().

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    return list(filter(is_prime, numbers))


def main():
    Data = input("Enter list : ")
    number_list = [int(num) for num in Data.split()]
    print("list : " ,number_list)

    prime_numbers = get_primes(number_list)
    print("Prime Numbers : " ,prime_numbers)

if __name__ == "__main__":
    main()

#OUTPUT
#Enter list : 10 11 12 13 14 15 16 17
#list :  [10, 11, 12, 13, 14, 15, 16, 17]
#Prime Numbers : [11, 13, 17]






            

    