#!/usr/bin/env python

VERBOSE = 0


def trace(*args):
    if VERBOSE: print(*args)
    

def solve_one(P):
    trace(P)
    if len(P) % 2 == 1:
        return '0'
    else:
        return '1\n0.0'


def solve(problem):
    lines = iter(problem.splitlines())
    T = int(next(lines))
    for i in range(T):
        N = int(next(lines))
        P = [int(next(lines)) for _ in range(N + 1)]
        sol = solve_one(P)
        print(f'Case #{i+1}: {sol}')


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    solve(data)