def check_prime():
   
    number = int(input("Enter a positive integer greater than 1: "))

    if number <= 1:
        print(f"{number} is not a prime number.")
    else:
      
        for i in range(2, number):
          
            if number % i == 0:
                print(f"{number} is not a prime number. It is divisible by {i}.")
                break
        else:
            print(f"{number} is a prime number.")


check_prime()
check_prime()
check_prime()

