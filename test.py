import math

def fun(x):
    mmax = math.floor((math.sqrt(4 * float(x) + 1) - 1) / 2)
    xbase = mmax * ( mmax + 1 )
    n = 2 * mmax + math.ceil((x - xbase) / (mmax + 1))
    return n

with open('file.txt', 'r') as f:
    steps = int(f.readline())
    for x in xrange(0, steps):
        a, b = map(int, f.readline().split(' '))
        n = fun(b - a)
        print('n = %d' % n)

