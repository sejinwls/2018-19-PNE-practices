a_count=0
c_count=0
g_count=0
t_count = 0
lenght=0
filename= input("Please introduce a file name ")
data = open (filename, "r")
for line in data:
    line.replace(" ", "")
    a_count += line.count("A")
    c_count += line.count("C")
    g_count += line.count("G")
    t_count += line.count("T")
    lenght += len(line.replace(" ","").replace("\n", ""))
print("Total lenght:",lenght)
print("A:", a_count)
print("C:", c_count)
print("G:", g_count)
print("T:", t_count)
