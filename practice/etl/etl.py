def transform(old):
    new = {}
    for point, letters in old.items():
        for letter in letters:
            new[letter.lower()] = point
    return new