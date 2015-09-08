def distance(string, string2):
    hamming = 0
    for a, b in zip(string, string2):
            if a != b:
                hamming +=1
    return hamming
