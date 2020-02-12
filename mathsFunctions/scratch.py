import math
import generatePrimes

prime_list = list()
prime_list = generatePrimes(1, math.sqrt(1809123481293571209851794))

for num in range(prime_list):
    print(prime_list[num])