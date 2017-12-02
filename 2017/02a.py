test = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8],
]

c = lambda s: sum(max(r)-min(r) for r in s)

print(c(test)==18)

with open('02.txt') as f:
    s=f.read()
    d=[[int(c) for c in l.split("\t")] for l in s.strip().split("\n")]
    print(d)
    print(c(d))
