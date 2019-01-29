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
total_sum = 1
if term == 1:
    total_sum = 0
elif term == 2:
    total_sum = 1
elif term > 2:
    for i in range(3, term+1):
        b = fibonacci(i)
        total_sum += b
print("The value of the sum is ", total_sum)
