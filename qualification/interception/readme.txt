Consider an N-degree polynomial, expressed as follows:

P[N] * x^N + P[N-1] * x^N-1 + ... + P[1] * x^1 + P[0] * x^0

You'd like to find all of the polynomial's x-intercepts — in other words, all
distinct real values of x for which the expression evaluates to 0.

Unfortunately, the order of operations has been reversed: Addition (+) now has
the highest precedence, followed by multiplication (*), followed by
exponentiation (^). In other words, an expression like ab + c * d should be
evaluated as a((b+c)*d). For our purposes, exponentiation is right-associative
(in other words, abc = a(bc)), and 00 = 1. The unary negation operator still has
the highest precedence, so the expression -2-3 * -1 + -2 evaluates to -2(-3 *
(-1 + -2)) = -29 = -512.

Input

Input begins with an integer T, the number of polynomials. For each polynomial,
there is first a line containing the integer N, the degree of the polynomial.
Then, N+1 lines follow. The ith of these lines contains the integer Pi-1.

Output

For the ith polynomial, print a line containing "Case #i: K", where K is the
number of distinct real values of x for which the polynomial evaluates to 0.
Then print K lines, each containing such a value of x, in increasing order.

Absolute and relative errors of up to 10^-6 will be ignored.

Constraints
1 ≤ T ≤ 200 
0 ≤ N ≤ 50 
-50 ≤ Pi ≤ 50 
PN ≠ 0 

Explanation of Sample

In the first case, the polynomial is 1 * x1 + 1 * x0. With the order of
operations reversed, this is evaluated as (1 * x)(((1 + 1) * x)0), which is
equal to 0 only when x = 0.

In the second case, the polynomial does not evaluate to 0 for any real value x.
