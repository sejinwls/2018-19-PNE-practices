def sum(n):
    sum=0
    for i in range(n+1) :
        sum += i
    return sum
number= int(input("Please introduce an integer number"))
total_sum= sum(number)
print("The total sum is", total_sum)
