import sys

x, y, w, s = list(map(int, sys.stdin.readline().split()))

max_xy = max(x, y)
min_xy = min(x, y)

diag_line = min_xy*s + (max_xy-min_xy)*w
line_only = (x+y)*w

diag = (x+y)//2
diag_rev = min(abs(x-diag), abs(y-diag))

if abs(x-diag) == abs(y-diag):
    line = 0
else:
    if abs(x-diag-diag_rev) == 0:
        line = abs(y-diag-diag_rev)
    else:
        line = abs(x-diag-diag_rev)

diag_diag = (diag+diag_rev)*s + line*w

time = min(diag_line, line_only, diag_diag)

print(time)