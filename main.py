
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

number = int(input("Enter a positive integer: "))

if number < 0:
    print("Invalid number")

else:
    print("Fibonacci sequence: ")
    for i in range(0, number):
        print(fibonacci(i))
