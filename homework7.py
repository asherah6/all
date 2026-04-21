# Task 1
# Write a recursive function for finding the greatest common divisor of two integers.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
print(gcd(100, 75))

