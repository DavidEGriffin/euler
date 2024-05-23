# Problem 3

The prime factors of 
13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

## Solution

While brute force could solve this problem too, I'm ready for some elegance.

We can split up 600851475143 into its prime factorization

    600851475143 = f1 * f2 * ... * fn

where f1 ≤ f2 ≤ ... ≤ fn.

If we find the smallest prime factor, f1, and divide it from 600851475143, we are left with

    600851475143 / f1 = f2 * f3 * ... * fn

We can continue by finding the smallest prime factor of the quotient, f2. If we divide f2
from our quotient, we get

    600851475143 / f1 / f2 = f3 * f4 * ... * fn

We can continue this process until we are left with nothing but the largest prime factor of
600851475143, fn

    600851475143 / f1 / f2 / ... / f(n-1) = fn

We will know we have reached fn by repeating the process one more time, and finding we are left with only 1

    600851475143 / f1 / f2 / ... / fn = 1

I will implement this algorithm in Python.

`python`

```
>>> def is_prime(number: int):
...     for i in range(2, number//2):
...         if number % i == 0:
...             return False
...     return True
... 
>>> def least_prime_factor(number: int):
...     for i in range(2, number//2):
...         if number % i == 0 and is_prime(i):
...             return i
...     return number
... 
>>> number = 600851475143
>>> factor = 1
>>> while number > 1:
...     factor = least_prime_factor(number)
...     number //= factor
... 
>>> answer = factor
>>> print(answer)
6857
```