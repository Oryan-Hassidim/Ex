
def get_next_row(row):
    new_row = [1]
    for i in range(1, len(row)):
        new_row.append(row[i-1] + row[i])
    new_row.append(1)
    return new_row

def pasc_row(n):
    row = [1]
    for _ in range(1, n):
        row = get_next_row(row)
    while True:
        row = get_next_row(row)
        yield row

g = pasc_row(3)
next(g)
next(g)
next(g)


