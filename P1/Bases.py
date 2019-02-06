
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
