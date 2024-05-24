# Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
1 to 20?

## Solution

Consider the following obvious statements.

(1) A number *a* is evenly divisible by *b* if and only if *b* is a factor of *a*.

(2) A number *b* is a factor of *a* if and only if the factors of *b* are factors of *a*.

From (2) we get a corollary:

(3) A number *b* is a factor of *a* if and only if the prime factors of *b* are prime factors of *a*.

We need a number *a* that evenly divides all *b*=1 to 20, so by (1) it suffices to find a number *a* such that for all *b*=1 to 20, *b* is a factor of *a*.
By (3), we need a number such that the prime factors of *b* are prime factors of *a* for *b*=1
to 20.

    1 = 1
    2 = 2
    3 = 3
    4 = 2 * 2
    5 = 5
    6 = 2 * 3
    7 = 7
    8 = 2 * 2 *2
    9 = 3 * 3
    10 = 2 * 5
    11 = 11
    12 = 2 * 2 * 3
    13 = 13
    14 = 2 * 7
    15 = 3 * 5
    16 = 2 * 2 * 2 * 2
    17 = 17
    18 = 2 * 3 * 3
    19 = 19
    20 = 2 * 2 * 5

Since prime factors can have repetitive elements (e.g. 20 = 2 x 2 x 5),
to get *a* we will take the number whose prime factorization is the union of the multiset
of prime factors of *b*=1 to 20.

The union of the multisets of these prime factors is the multiset which contains all the
elements from every multiset with the maximum multiplicity from any one multiset.

    {
        2 (mult: 4),
        3 (mult: 2),
        5 (mult: 1),
        7 (mult: 1),
        11 (mult: 1),
        13 (mult: 1),
        17 (mult: 1),
        19 (mult: 1)
    }

We will use Python to quick calculate the number with this factorization.

`python`
```
>>> answer = (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19
>>> print(answer)
232792560
```