import sys
import math

a_u, a_d = list(map(int, sys.stdin.readline().split()))
b_u, b_d = list(map(int, sys.stdin.readline().split()))

c_d = math.lcm(a_d, b_d)

c_u = a_u*(c_d//a_d) + b_u*(c_d//b_d)

gcd = math.gcd(c_u, c_d)

print(c_u//gcd, c_d//gcd)