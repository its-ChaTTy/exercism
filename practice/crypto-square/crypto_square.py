import math
import re

def cipher_text(plain_text):
    plain_text = re.sub(r'\W+', '', plain_text).lower()

    if not plain_text:
        return ""

    c = math.ceil(math.sqrt(len(plain_text)))
    r = len(plain_text) // c
    if len(plain_text) % c != 0:
        r += 1

    rows = []
    for i in range(r):
        row = plain_text[i*c:(i+1)*c].ljust(c)
        rows.append(row)

    encoded_text = ""
    for i in range(c):
        for row in rows:
            encoded_text += row[i]

    chunks = []
    for i in range(c):
        chunk = encoded_text[i*r:(i+1)*r]
        chunks.append(chunk)

    return ' '.join(chunks)