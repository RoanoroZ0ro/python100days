def prime_checker(number):

    if number <= 1:
        print("It's not a prime number.")
        return None

    num_of_divisors = 0

    for i in range(1, number+1):
        if number % i == 0:
            num_of_divisors += 1

    if num_of_divisors != 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
    return None


for i in range(20):
    print(i)
    print(prime_checker(i))
