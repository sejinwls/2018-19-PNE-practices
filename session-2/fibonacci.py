def fibonacci(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return c


term = int(input("Please introduce the number of the term: "))
value = fibonacci(term)
print("The value for that term is ", value)
