def is_prime(number: int):
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True

def least_prime_factor(number: int):
    for i in range(2, number//2):
        if number % i == 0 and is_prime(i):
            return i
    return number

number = 600851475143
factor = 1
while number > 1:
    factor = least_prime_factor(number)
    number //= factor

answer = factor
print(answer)