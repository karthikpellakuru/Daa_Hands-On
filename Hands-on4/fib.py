#Question : Implement the Fibonacci sequence

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

n = int(input("Enter any value to calculate Fibonacci sequence(n): "))

result = fib(n)
print(f"Fibonacci({n}): {result}")

---OUTPUT---
Enter value to calculate Fibonacci sequence(n): 5
fibonacci( 5 ): 5

Process finished with exit code 0
