#!/usr/bin/env python


VERBOSE = False

def trace(*args):
    if VERBOSE: print(*args)
    

def solve_one(A, K, V):
    N = len(A)
    k = (K * (V - 1)) % N
    xs = sorted((i + k) % N for i in range(K))
    return ' '.join(A[i] for i in xs)


def solve(problem):
    lines = iter(problem.splitlines())
    T = int(next(lines))
    for i in range(T):
        N, K, V = map(int, next(lines).split())
        A = [next(lines) for _ in range(N)]
        sol = solve_one(A, K, V)
        print(f'Case #{i+1}: {sol}')


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    solve(data)