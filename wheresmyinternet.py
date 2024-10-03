def addEdge(G, u, v, w):
    G.setdefault(u, {})[v] = w

def neighbors(G,u):
    """Return list of outgoing neighbors of vertex u"""
    return list(iter(G.get(u,())))   # works for set or dict

def bfs_visit(G, src, trace):
    """Perform BFS exploration of graph G starting at vertex src,
    recording the following relevant info in trace dictionary:

    trace[v] = (groupNum, parent, distance)

    groupNum designates vertices as part of current group
    parent is the parent of v in BFS tree
    distance is the number of steps from src to v in the BFS tree
    

    Note that entry for trace[src] will have None as the parent.
    """
    depth = 0
    trace[src] = (None, depth)
    Q = [src]                         # state for further exploration                                

    while Q:
        depth += 1   # NOTE: if limit on max depth, could return here                
        newQ = []
        for u in Q:
            for v in neighbors(G,u):  # function defined earlier!
                if v not in trace:    # new discovery                                                 
                    trace[v] = (u, depth)
                    newQ.append(v)
                    # NOTE: could return now if v == goal
        Q = newQ

line = input()
line = line.split()
numHouses = int(line[0])
numCables = int(line[1])

runGraph = { j:{} for j in range(1,1+numHouses) } 

didntFind1 = True

for i in range(numCables):
    line = input()
    line = line.split()
    if int(line[0]) == 1:
        didntFind1 = False
    addEdge(runGraph, int(line[0]), int(line[1]), 1)
    addEdge(runGraph, int(line[1]), int(line[0]), 1)

if didntFind1:
    addEdge(runGraph, 1, 1, 1)


trace = {}
bfs_visit(runGraph, 1, trace)

wantReturn = []

for i in range(1, numHouses+1):
    if i not in trace:
        wantReturn.append(i)

if not wantReturn:
    print('Connected')
else:
    for house in wantReturn:
        print(house)
