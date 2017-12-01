test = {
  '1122':     3,
  '1111':     4,
  '1234':     0,
  '91212129': 9,
}

import re
c=lambda s:sum(int(u[0])for u in re.findall('\d\d',''.join([t+t for t in s[-1]+s])[1:-1]) if u[0] == u[1])
c=lambda s:sum(int(u[0])for u in[(s+s)[i]+(s+s)[i+1]for i in range(len(s))]if u[0] == u[1])

for a, b in test.items():
    print("%s => %s == %s => %s" % (a, c(a), b, c(a) == b))

with open('01.txt') as f:
    print(c(f.read().strip()))
