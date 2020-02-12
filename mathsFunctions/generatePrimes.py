def generate_primes(start, end):
    if end < start:
        return "End must be greater than start"
    prime_list = list()
    if start < 5:
        prime_list.append(2)
        prime_list.append(3)
    init_val = start/6
    for num in range(init_val, end):
        minus_one = 6 * num - 1
        plus_one = 6 * num + 1
        if start <= minus_one < end:
            if check_sieve_value(minus_one):
                prime_list.append(minus_one)

        if start <= plus_one < end:
            if check_sieve_value(plus_one) > 0:
                prime_list.append(plus_one)

    return prime_list


def check_sieve_value(value):
    if (value != 5 and value != 7) and (value % 7 == 0 or value % 5 == 0):
        return 0
    else:
        return value


int_list = generate_primes(input("Enter the start value: \n"), (input("Enter the end value: \n")))

#print_string = ""
#print(print_string.join(str(int_list)))
print(str(int_list))