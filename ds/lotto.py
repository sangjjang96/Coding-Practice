import sys
from itertools import *

while True:
    in_txt = list(map(int, sys.stdin.readline().split()))
    
    if in_txt[0] == 0:
        break
    
    numbers = in_txt[1:]
    
    result = list(combinations(numbers, 6))
    result.sort()
    
    for r in result:
        print(*r)
    print()