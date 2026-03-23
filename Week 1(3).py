def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

for num in even_numbers(20):
    print(num)