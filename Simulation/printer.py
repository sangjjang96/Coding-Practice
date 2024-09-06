from queue import PriorityQueue

T = int(input())

for _ in range(T):
    N, Q = list(map(int, input().split()))

    q = PriorityQueue()

    l = list(map(int, input().split()))
    
    for idx, pri in enumerate(l):
        q.put((10-pri, idx))

    for _ in range(len(l)):
        print(q.get())