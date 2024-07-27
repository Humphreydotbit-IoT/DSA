#adjacency list

graph = {
    '1' : ['2'],
    '2' : ['7', '4'],
    '3' : ['4'],
    '4' : ['6'],
    '5' : ['4', '3'],
    '6' : [],
    '7' : ['5']
}

visited = set()

def DFS(graph, s):
    if s not in visited:
        print(s, "--->", end="")  #our answer
        visited.add(s)
        for neighbor in graph[s]:
            DFS(graph, neighbor)
              
                
DFS(graph, '1')


