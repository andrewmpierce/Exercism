# def distance(string, string2):
#     hamming = 0
#     for a, b in zip(string, string2):
#             if a != b:
#                 hamming +=1
#     return hamming

def distance(string, string2):
    hamming = 0
    for idx, nucleotide in enumerate(string):
        if string[idx] != string2[idx]:
            hamming += 1
    return hamming
