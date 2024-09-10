#Question: Will it effect your results from #1?

def f1(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
            y = i + j
    return x

def f2(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

result_f1 = f1(3)
result_f2 = f2(3)

print("Result of f1:", result_f1)
print("Result of f2:", result_f2)

Output:
Result of f1: 10
Result of f2: 10
