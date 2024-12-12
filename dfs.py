def dfs(g,n , visited):
    if n not in visited:
        print(n, end= '')
        visited.add(n)
        for neighbour in g[n]:
            dfs(g, neighbour, visited)

g = {0:[1,2], 1:[3], 2:[4,5], 3:[], 4:[], 5:[]}
n = 0
visited = set()
dfs(g,n,visited)
