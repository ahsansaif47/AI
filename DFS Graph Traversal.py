
class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

graphA={'O' : Node('O', None, ['Z','S'], None),
       'Z' : Node('Z', None, ['A','O'], None),
       'A' : Node('A', None, ['Z','S','T'], None),
       'S' : Node('S', None, ['A','O','F','R'], None),
       'T' : Node('T', None, ['A','L'], None),
       'L' : Node('L', None, ['T','M'], None),
       'R' : Node('R', None, ['S','C','P'], None),
       'M' : Node('O', None, ['D','L'], None),
       'F' : Node('F', None, ['S','B'], None),
       'D' : Node('D', None, ['M','C'], None),
       'C' : Node('C', None, ['R','P','D'], None),
       'P' : Node('P', None, ['B','R','C'], None),
       'B' : Node('B', None, ['G','P','F'], None),
       'G' : Node('G', None, ['B'], None),
       }

def DFS(smGraph, iniState):
    frontier = [iniState]
    explored = []

    while len(frontier) != 0:
        currNode = frontier.pop(len(frontier)-1)
        explored.append(currNode)
        for ver in smGraph[currNode].actions:
            if (len(smGraph[currNode].actions)) == 0:
                break
            elif ver in explored or ver in frontier:
                continue
            frontier.append(ver)
            smGraph[ver].parent = currNode

    print(explored)

print("DFS Complete Graph Traversal : ")
DFS(graphA, 'O')


