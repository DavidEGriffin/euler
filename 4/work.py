def digits(number: int) -> list:
    """List the digits of a natural number from left to right."""
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits

def is_palindrome(number: int) -> bool:
    """Return whether a natural number is a palindrome."""
    num_digits = len(digits(number))
    for i in range(num_digits // 2):
        if digits(number)[i] != digits(number)[-1-i]:
            return False
    return True

biggest = 0
for a in range(999, 99, -1):
    if a ** 2 < biggest:
        break
    for b in range(a, 99, -1):
        if is_palindrome(a * b):
            biggest = a * b
            break
        if a * b < biggest:
            break

print(biggest)