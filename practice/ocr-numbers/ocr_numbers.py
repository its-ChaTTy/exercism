def process_section(section, digits):
    chunks = [''.join(row[i:i+3] for row in section) for i in range(0, len(section[0]), 3)]
    output = [digits.get(chunk, '?') for chunk in chunks]
    return ''.join(output)

def convert(input_grid):
    digits = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    sections = [input_grid[i:i+4] for i in range(0, len(input_grid), 4)]
    return ','.join(process_section(section, digits) for section in sections)