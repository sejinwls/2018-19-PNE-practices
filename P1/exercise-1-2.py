from Bases import count_bases

# Main program
s = input("Enter the sequence: ")
dictionary = count_bases(s)

# Calculate the total sequence lenght
tl = len(s)
print("This sequence is", tl, " bases in length")

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
