
def to_rna(string):
    string = list(string)
    counter = 0
    for nucleotide in string:
        if nucleotide == 'G':
            string[counter] = 'C'
        elif nucleotide == 'C':
            string[counter] = 'G'
        elif nucleotide == 'T':
            string[counter] = 'A'
        elif nucleotide == 'A':
            string[counter] = 'U'
        counter += 1
    rna = ''.join(string)
    return rna

to_rna('A')
to_rna('GAA')
