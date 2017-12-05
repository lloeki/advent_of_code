# find cell count of square containing value
# walk from cell count value to nearest axis

# radius to cell count
# r=0 c=1   (2*0+1)**2=1
# r=1 c=9   (2*1+1)**2=9
# r=2 c=25  (2*2+1)**2=25
#     c     (2*r+1)**2
# r         (sqrt(c)-1)/2

# radius to axis
# - square filled at bottom right
# - first vertical axis is a radius away
# - each vertical axis is then two radius away, three times
# r=0 c=1  a1=1  a2=1  a3=1  a4=1
# r=1 c=9  a1=8  a2=6  a3=4  a4=2
# r=2 c=25 a1=23 a2=19 a3=15 a4=11
# c-r      a1
# c-r-2*r        a2
# c-r-2*r-2*r          a3
# c-r-2*r-2*r-2*r            a4

def r2c(r):
    return (2*r+1)**2

def v2d(v):
    r=0
    c=1
    while v>c:
        r+=1
        c=r2c(r)
    return [c, r, r+min([abs(c-r-v), abs(c-3*r-v), abs(c-5*r-v), abs(c-7*r-v)])]

c, r, d = v2d(277678)
print("c=%s r=%s d=%s" % (c, r, d))
