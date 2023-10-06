"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError(f'{number_of_primes} is less than or equal to zero so can\'t be prime')
    num = 2

    while len(list) < number_of_primes:
        if num <= 3:
            is_prime = True
        else:
            if num % 2 == 0 or num % 3 == 0:
                is_prime = False
            else:
                is_prime = True
                i = 5
                while i * i <= num:
                    if num % i == 0 or num % (i + 2) == 0:
                        is_prime = False
                        break
                    i = i + 6

        if is_prime:  # No need to check == True, it's redundant
            list.append(num)

        num = num + 1

    return list
