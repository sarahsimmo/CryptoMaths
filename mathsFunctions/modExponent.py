import isPrime


def calc_exponent(number, exponent):
    return number ** exponent


def calc_modulus(num_value, mod_value):
    return num_value % mod_value


def calc_result(num, exp, mod):
    while not (isPrime.is_prime(mod)):
        mod = (int(input("Modulus must be a prime number - please enter a new value: \t")))
    result = calc_exponent(num, exp)
    result = calc_modulus(result, mod)
    return result


while True:
    number = input("Enter number: \t")
    if number == "exit":
        break
    else:
        number = int(number)
    exponent = int(input("Enter exponent: \t"))
    modulus = int(input("Enter modulus: \t"))
    print(calc_result(number, exponent, modulus))
