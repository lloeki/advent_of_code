test = {
  '1212':     6,
  '1221':     0,
  '123425':   4,
  '123123':  12,
  '12131415': 4,
}

c=lambda s:sum(int(u[0])for u in[(s+s)[i]+(s+s)[i+len(s)//2]for i in range(len(s))]if u[0]==u[1])

for a, b in test.items():
    print("%s => %s == %s => %s" % (a, c(a), b, c(a) == b))

with open('01.txt') as f:
    print(c(f.read().strip()))
