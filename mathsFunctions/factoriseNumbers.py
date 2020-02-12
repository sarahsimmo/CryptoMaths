import isPrime


def next_prime(current_prime):
    counter = current_prime + 1
    while not isPrime.is_prime(counter):
        counter += 1
    return counter


def factorise(number):
    prime = 2
    # Base case
    while number > 1:
        if number == 1:
            break
        if number % prime == 0:
            print(prime)
            number = number // prime
        else:
            prime = next_prime(prime)


factorise(int(input("Enter a number: \t")))
