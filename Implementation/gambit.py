import sys

king_pawn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

h, w, n, k, a, b = list(map(int, sys.stdin.readline().split()))

white = []
black = []

for i in range(2*n+2):
    typ, x, y = list(map(int, sys.stdin.readline().split()))
    
    if typ[0] == 'K':
        white.append([typ, x, y])
    elif typ[0] == 'P':
        white.append([typ, x, y])
    elif typ[0] == 'k':
        black.append([typ, x, y])
    elif typ[0] == 'p':
        black.append([typ, x, y])
        
        