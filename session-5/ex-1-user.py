def count_a(seq):
    """"THis function is for counting the number of A's in the sequence"""

    # Counter for the As
    result = 0

    for b in seq:
        if b == "A":
            result += 1

    # Return the result
    return result


# Main program
s = input("Enter the sequence: ")
na = count_a(s)


# Calculate the total sequence lenght
tl = len(s)
print("This sequence is", tl," bases in length")

# Calculate the percentage of As in the sequence
if tl > 0:
    perc = round(100.0 * na/tl, 1)
else:
    perc = 0
print("The total lenght is: {}".format(tl))
print("The percentage of As is {}%".format(perc))
