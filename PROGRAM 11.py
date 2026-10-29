
import math

total_keys = math.factorial(25)
power = math.log2(total_keys)

print("Total possible Playfair keys:", total_keys)
print("Approximate power of 2: 2^", round(power, 2))
