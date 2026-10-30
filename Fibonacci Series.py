n = int(input("Enter the number of terms: "))
a = 0
b = 1
fib = []
for i in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci Series:")
print(*fib, sep=", ")
