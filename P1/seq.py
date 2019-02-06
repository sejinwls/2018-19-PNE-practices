class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence created")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comp_seq = ""
        for b in self.strbases:
            comp_seq = comp_seq + comp[b]
        return comp_seq

    def reverse(self):
        rev_seq = ""
        for b in self.strbases:
            rev_seq = b + rev_seq
        return rev_seq

    def count(self, base):
        counter = self.strbases.count(base)
        return counter

    def perc(self, base):
        tl = len(self.strbases)
        counter = self.strbases.count(base)
        perc = 100.0 * counter/tl
        return perc


