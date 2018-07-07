#!/usr/bin/env python


VERBOSE = False

def trace(*args):
    if VERBOSE: print(*args)
    

def solve_one(A, K, V):
    res = [(0, i) for i in range(len(A))]
    period = list()
    period.append(list(res))
    
    visited = set()
    visited.add(tuple(i for _, i in res))
    trace(res)
    
    for _ in range(V - 1):
        res[:K] = [(x + 1, i) for x, i in res[:K]]
        res = sorted(res)
        
        p = tuple(i for _, i in res)
        if p in visited:
            trace('period', len(period), period)
            res = period[(V - 1) % len(period)]
            trace('res:', res)
            break
            
        trace(res)
        visited.add(p)
        period.append(list(res))
    
    xs = sorted(i for _, i in res[:K])
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