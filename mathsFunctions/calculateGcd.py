def divide(a, b):
    return a % b


def calculate_gcd(first_number, second_number):
    if first_number < second_number:
        big = second_number
        small = first_number
    else:
        big = first_number
        small = second_number
    remainder = small

    while remainder > 1:
        remainder = divide(big, small)
        if remainder == 0:
            return small
        else:
            big = small
            small = remainder
    return remainder

while True:
    print(calculate_gcd(int(input("Enter first number \t")), int(input("Enter second number \t"))))