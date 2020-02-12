def is_prime(number):
    divisor = number // 2
    while divisor >= 2:
        if number % divisor == 0:
            return False
        else:
            divisor -= 1
    return True
