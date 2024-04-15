def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        triangle = rows(row_count - 1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle