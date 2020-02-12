def generate_sequence(seed, base, add_factor, modulus):
    # Using (base x 'seed' + add_factor) mod modulus, where each new seed is the previous calculated value.
    new_seed = seed
    for i in range(20):
        new_seed = (base * new_seed + add_factor) % modulus
        print new_seed


def add_input():
    seed = int(input("Enter seed: \t"))
    base = int(input("Enter base number \t"))
    add_factor = int(input("Enter addition factor: \t"))
    modulus = int(input("Enter modulus value: \t"))
    generate_sequence(seed, base, add_factor, modulus)


while add_input() != "exit":
    add_input()
