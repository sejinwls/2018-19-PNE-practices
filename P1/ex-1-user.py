def count_bases(seq):
    """"THis function is for counting the number of A's in the sequence"""

    # Counter for the As
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1


    # Return the result
    return count_a, count_c, count_g, count_t


# Main program
s = input("Enter the sequence: ")
a,c,g,t = count_bases(s)


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
