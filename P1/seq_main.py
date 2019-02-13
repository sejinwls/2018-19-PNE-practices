from seq import Seq
# Program that creates and prints information about sequences

s1 = Seq("ACGT")
s2 = Seq("GTCAGTCA")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

seqs = [s1, s2, s3, s4]
index = 1
for seq in seqs:
    print("""Sequence""", index, """: """, seq.strbases, """
    Length:{}""".format(s1.len()), """
    Bases count:  A:{}""".format(seq.count("A")), """C:{}""".format(seq.count("C")), """G:{}""".format(seq.count("G")), """T:{}""".format(seq.count("T")), """
    Bases percentage: A:{}""".format(seq.perc("A")), """C:{}""".format(seq.perc("C")), """G:{}""".format(seq.perc("G")), """T:{}""".format(seq.perc("T")))
    index += 1
