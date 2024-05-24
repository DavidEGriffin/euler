# Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Solution

Once again, this problem could be brute forced, but I took a more
efficient approach.

Clearly, the largest palindrome should be a combination of fairly large numbers.
Recall that for two 2-digit numbers, the highest combination was 91 x 99.
So, I decided to work my way backwards from 999 x 999. I devised the following algorithm:

Let *a*, *b* = 999. Check whether (*a * b*) is a palindrome. If not, decrement *b* by 1, and
check again. Continue until the first palindrome is found, or *b* reaches the smallest 3-digit number (100).

Next, let *a*, *b* = 998. Once again decrement *b* until either we find a palindrome
greater than our previous greatest palindrome, or *a * b* is less than our previous greatest palindrome. Note that we have already checked whether 998 * 999 is a palindrome, so we can begin with 998 * 998.

Continue the process with the next numbers *a*, *b* = 997, and so on, taking note if a
palindrome greater than our previous record high is found.

Once we have reached the point where *a*^2 is less than our record high palindrome, we can
cut short execution of the algorithm, as it is no longer possible to find a greater palindrome.

I implemented this algorithm in Python.

`python`
```
>>> biggest = 0
>>> for a in range(999, 99, -1):
...     if a ** 2 < biggest:
...         break
...     for b in range(a, 99, -1):
...         if is_palindrome(a * b):
...             biggest = a * b
...             break
...         if a * b < biggest:
...             break
... 
>>> print(biggest)
906609
```