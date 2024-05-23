# Problem 1

If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Solution

A brute force approach to this problem works just fine; it is trivial
to check whether a number is a multiple of 3 or 5.

`python`
```
>>> multiples = [
...     number for number in range(1, 1000)
...     if number % 3 == 0 or number % 5 == 0
... ]
>>>
>>> answer = sum(multiples)
>>> print(answer)
233168
```

![alt text](<winning.png>)