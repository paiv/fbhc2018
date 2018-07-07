#!/usr/bin/env python

VERBOSE = 0


def trace(*args):
    if VERBOSE: print(*args)
    
    
def ethan(a, b):
    trace(a, 'in', b)
    i = j = 0
    while True:
        trace(i, j)
        if i >= len(a): return True
        if j >= len(b): return False
        if a[i] == b[j]:
            i += 1
            j += 1
        elif i == 0:
            j += 1
        else:
            i = 0
            

def solve_one(s):
    for i, x in enumerate(s[1:-1], 1):
        if x == s[0]:
            t = s[:i] + s
            if t[:len(s)] != s:
                assert not ethan(s, t)
                return t
    return 'Impossible'
    

def solve(problem):
    lines = iter(problem.splitlines())
    T = int(next(lines))
    for i in range(T):
        sol = solve_one(next(lines))
        print(f'Case #{i+1}: {sol}')


if __name__ == '__main__':
    # print(ethan('FBFBFA', 'FBFBFBFA'))
    # exit()
    
    import sys
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    solve(data)