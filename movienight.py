from heapq import *
import sys
sys.setrecursionlimit(10**6)

trials = int(input())
start = {

}

for n in range(trials):
    x = [int(test) for test in input().split()]
    start[n+1] = x

def neighbors(G,u):
    """Return list of outgoing neighbors of vertex u"""
    return list(iter(G.get(u,())))   # works for set or dict

def dfs_visit(G, src, trace, groupNum=0):
    """Computes one DFS tree for graph G starting at vertex src.
    trace must be a dictionary (possibly empty) for recording info
       trace[v] = (groupNum, parent)
    for all newly discovered v in this tree. src parent is None.

    Return two thing:
       list of visited vertices, ordered by "finish" time
       a pair (u,v) that is part of a cycle (or None if no cycle)
       
    If a cycle exists that contains src, it is reported.
    """
    trace[src] = (groupNum, None)
    stack = [ (src,neighbors(G,src)) ]
    active = {src}                      # vertex currently on stack
    finished = []
    cycle = None
    while stack:
        u,children = stack[-1]
        if children:
            v = children.pop()          # pick a child, any child
            if v not in trace:
                trace[v] = (groupNum, u)
                stack.append( (v,neighbors(G,v)) )
                active.add(v)
            elif v in active:  # likely cycle
                if v != u:     # NOTE: Remove this if directed graph
                    if cycle is None or cycle[1] != src:
                      cycle = (u,v)
        else:
            finished.append(u)
            active.remove(u)
            stack.pop()
    return finished,cycle


def dfs(G):
    """Compute DFS of all components of a graph.

    Returns four things:
    - number of DFS trees (i.e. connected components, if undirected)
    - order of vertices (a topological order if graph is acyclic)
    - An edge (u,v) that belongs to a cycle (None, if no cycle)
    - Trace dictionary that gives (groupNum, parent) for each vertex
    """
    trace = {}
    topo = []
    count = 0
    cycle = None
    for u in G:
        if u not in trace:
            finish,tempCycle = dfs_visit(G, u, trace, count)
            topo.extend(finish)
            count += 1
            if cycle is None: cycle = tempCycle
    topo.reverse()
    return count,topo,cycle,trace


def SCC(G):
    """Return list of strongly-connected components of directed G."""
    _,topo,_,_ = dfs(G)    # need topo order from run of DFS

    T = { u : set() for u in G}  # next, compute transpose graph of G
    for u in G:
        for v in G[u]:
            T[v].add(u)

    trace = {}
    count = 0
    for u in topo:             # dfs on T using topo for outer loop
        if u not in trace:
            dfs_visit(T, u, trace, count)
            count += 1
    result = [set() for _ in range(count)]
    for v in T:
        result[trace[v][0]].add(v) 
    return result

end = (SCC(start))

group = {}

for k in range(len(end)):
    for u in end[k]:
        group[u] = k

parent = {}
children = {}

#print(start)

for a in range(1,1+trials):
    b = start[a][0]
    ga = group[a]
    gb = group[b]
    if ga != gb:
        parent[ga] = gb
        children.setdefault(gb,[]).append(ga)

Z = 10**9 + 7

def count(j):
    if j in children:
        product = 1
        for c in children[j]:
            product = (product*count(c))%Z
        return 1+product
    else:
        return 2

total = 1
for g in range(len(end)):
    if g not in parent:
        temp = count(g)
        #print('===', g,temp)
        total = (temp*total)%Z

#print(parent, children)
print((total-1)%Z)
#print(group)

#answer= len(SCC(gdict))
#answer = pow(2,answer)-1
#print(answer)
