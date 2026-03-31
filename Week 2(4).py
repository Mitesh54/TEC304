result = list(
    map(
        lambda a, b, c: a + b + c,
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300]
    )
)

print(result)