test = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]

c = lambda s: sum([x // y for x in r for y in r if x / y == x // y and x != y][0] for r in s)

print(c(test)==9)

with open('02.txt') as f:
    s=f.read()
    d=[[int(c) for c in l.split("\t")] for l in s.strip().split("\n")]
    print(c(d))
