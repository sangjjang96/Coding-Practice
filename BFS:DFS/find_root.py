# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    
    visited = [0]*(101)
    ans = 0
    
    def dfs(x):
        global visited, graphs, ans
        
        visited[x] = 1
        
        if x == 99:
            ans = 1
            return
        
        for x_ in graphs[x]:
            if not visited[x_]:
                dfs(x_)
                
    idx, n = list(map(int, input().split()))
    
    edges = list(map(int, input().split()))
    
    graphs = [[] for _ in range(101)]
    
    for i in range(0, len(edges), 2):
        a, b = edges[i], edges[i+1]
        
        graphs[a].append(b)
        
    dfs(0)
    
    print(f'#{idx} {ans}')
    
    # ///////////////////////////////////////////////////////////////////////////////////