# use adjacency matrix (undirected)
# why undirected?
# use example 1
#0, 1, 2, 3, 4
G = [[0, 2, 2, 5, 3],
     [2, 0, 1, 4, 4],
     [2, 1, 0, 3, 5],
     [5, 4, 3, 0, 9],
     [3, 4, 5, 9, 0]]

INF = 9999
N   = 5

#r.key = 0
r   = 0

# put all vertex into the queue
# for each vertex
# set key = infinity
from heapdict import heapdict  # pip install heapdict or conda install heapdict

Q = heapdict()
for i in range(N):
    Q[i] = INF
Q[r] = 0

# set pi  = NIL
# pi = [None, None, None, None, None]
pi = [None] * 5
# set the pi of r = -1 or anything you like
pi[r] = -1
# print(f"PI: {pi}")

def adj(G, u):
    neighbors = []
    
    #for each vertex
    for v in range(N):
        #if G[u, v]
        if G[u][v]:
            #append to the neighbors
            neighbors.append(v)
    return neighbors

def v_in_Q(Q, v):
    #get the keys in Q
    keys = list(Q.keys())   #you can actually do if v in Q:
    #check if v in keys
    return v in keys

# while Q is not empty
while(Q):
    #u = extract_min  (dict has no extract_min)
    u  = Q.popitem()[0]  
    # for v in adj[u]
    for v in adj(G, u):
        # if v in Q, and w(u, v) < v.key
        if (v_in_Q(Q, v) and G[u][v] < Q[v]):
            #v.pi = u
            pi[v] = u
            #v.key = w(u, v)
            Q[v]  = G[u][v]
    
print(pi)
