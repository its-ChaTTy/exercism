def annotate(minefield):
    if not minefield:
        return []

    if not all(len(row) == len(minefield[0]) for row in minefield) or any(c not in ' *' for row in minefield for c in row):
        raise ValueError("The board is invalid with current input.")
    
    rows, cols = len(minefield), len(minefield[0])
    counts = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < rows and 0 <= j+dj < cols:
                            counts[i+di][j+dj] += 1
    
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                counts[i][j] = '*'
            elif counts[i][j] == 0:
                counts[i][j] = ' '
            else:
                counts[i][j] = str(counts[i][j])
    
    return [''.join(row) for row in counts]