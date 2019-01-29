a_count=0
c_count = 0
g_count = 0
t_count = 0
f = open("CPLX2.txt", "r")
for line in f:
    if not(line.startswith(">")):
        a_count += line.count("A")
        c_count += line.count("C")
        g_count += line.count("G")
        t_count += line.count("T")
print("A:",a_count)
print("C:",c_count)
print("G:",g_count)
print("T:",t_count)