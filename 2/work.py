fibonacci = [1, 2]
while fibonacci[-1] < 4_000_000:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

evens = [
    number for number in fibonacci
    if number % 2 == 0
]

answer = sum(evens)
print(answer)