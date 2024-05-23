multiples = [
    number for number in range(1, 1000)
    if number % 3 == 0 or number % 5 == 0
]

answer = sum(multiples)
print(answer)