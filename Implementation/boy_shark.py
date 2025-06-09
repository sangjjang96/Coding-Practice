import sys
import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, d_shark, eat):
    global ans, board, fish
    
    move_fish(x, y)
    
    while True:
        x_new, y_new = x + dx[d_shark], y + dy[d_shark]
        
        if not 0 <= x_new < 4 or not 0 <= y_new < 4:
            ans = max(ans, eat)
            return
        if not board[x_new][y_new]:
            x, y = x_new, y_new
            continue
        
        board_tmp, fish_tmp = copy.deepcopy(board), copy.deepcopy(fish)
        
        dir, num = fish[board[x_new][y_new][0]], board[x_new][y_new]
        fish[board[x_new][y_new][0]], board[x_new][y_new] = [], []
        
        dfs(x_new, y_new, num[1], eat + num[0] + 1)
        
        board, fish = board_tmp, fish_tmp
        fish[board[x_new][y_new][0]], board[x_new][y_new] = dir, num
        x, y = x_new, y_new

def move_fish(x_shark, y_shark):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            
            for _ in range(9):
                d = board[x][y][1]
                x_new, y_new = x + dx[d], y + dy[d]
                
                if not 0 <= x_new < 4 or not 0 <= y_new < 4 or (x_new == x_shark and y_new == y_shark):
                    board[x][y][1] = (board[x][y][1] + 1) % 8
                    continue
                    
                if board[x_new][y_new]:
                    fish[board[x_new][y_new][0]] = [x, y]
                
                board[x_new][y_new], board[x][y] = board[x][y], board[x_new][y_new]
                fish[i] = [x_new, y_new]
                break
                

board = [[] for _ in range(4)]
fish = [[] for _ in range(16)]

for i in range(4):
    infos = list(map(int, sys.stdin.readline().split()))
    
    for j in range(0, 7, 2):
        num, direc = infos[j], infos[j+1]
        
        board[i].append([num-1, direc-1])
        fish[num-1] = [i, j//2]

ans = 0
d_shark, eat = board[0][0][1], board[0][0][0] + 1
fish[board[0][0][0]], board[0][0] = [], []

dfs(0, 0, d_shark, eat)
print(ans)