def hamming_distance(text1, text2):
    return sum([1 for char1, char2 in zip(text1, text2) if char1 != char2])

