def count_bases(seq):
    """"THis function is for counting the number of bases in the sequence"""

    # Counter for the bases
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    # List of all bases
    bases = ["A", "C", "G", "T"]

    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1
    counts = [count_a, count_c, count_g, count_t]

    # Dictionary with bases and times they appear int he sequence
    b = dict(zip(bases, counts))
    # Return the dictionary
    return b


# Main program
s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")
seqs = [s1, s2]
seqs_name = ["Sequence 1", "Sequence 2"]
index = 0
for s in seqs:
    dictionary = count_bases(s)

    # Calculate the total sequence lenght
    tl = len(s)
    print("\n")
    print(seqs_name[index], "is", tl, "bases in length")

    if tl > 0:
        print("""Base A
        Counter: """, dictionary["A"], """
        Percentage: """, round(100.0 * dictionary["A"] / tl, 1))
        print("""Base C
        Counter: """, dictionary["C"], """
        Percentage: """, round(100.0 * dictionary["C"] / tl, 1))
        print("""Base G
        Counter: """, dictionary["G"], """
        Percentage: """, round(100.0 * dictionary["G"] / tl, 1))
        print("""Base T
        Counter: """, dictionary["T"], """
        Percentage: """, round(100.0 * dictionary["T"] / tl, 1))
    # Calculate the percentage of As in the sequence
    else:
        print("""Base A
        Counter: 0
        Porcentage: 0
    
    Base C
        Counter: 0 
        Porcentage: 0
    Base G
        Counter: 0 
        Porcentage: 0
    Base T
        Counter: 0 
        Porcentage: 0""")
    index += 1
