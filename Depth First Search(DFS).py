

class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self. actions = actions
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
graphB={'A' : Node('A', None, ['B','C','E'], None),
       'B' : Node('B', None, ['A','D','E'], None),
       'C' : Node('C', None, ['A','F','G'], None),
       'D' : Node('D', None, ['B','E'], None),
       'E' : Node('E', None, ['A','B','D'], None),
       'F' : Node('F', None, ['C'], None),
       'G' : Node('G', None, ['C'], None)
       }

graphC={
       'A' : Node('A', None, ['C','B'],0),
       'B' : Node('B', None, ['E','D'],0),
       'C' : Node('C', None, ['G','F'],0),
       'D' : Node('D', None, [], 0),
       'E' : Node('E', None, ['H'],0),
       'F' : Node('F', None, ['K'],0),
       'G' : Node('G', None, ['C'],0),
       'H' : Node('H', None, ['J','I'],0),
       'I' : Node('I', None, ['K'],0),
       'J' : Node('J', None, [], 0),
       'K' : Node('K', None, [], 0)
       }

def DFS(smGraph, initState, goalSt):
    iniState = initState
    frontier = [iniState]

    explored = []

    while len(frontier) != 0:
        currNode = frontier.pop(len(frontier)-1)
        explored.append(currNode)

        if currNode == goalSt:
            return pathTaken(smGraph, initState, goalSt)

        for ver in smGraph[currNode].actions:
           if ver in explored or ver in frontier:
               continue
           frontier.append(ver)
           smGraph[ver].parent = currNode
           
def pathTaken(smGraph, iniState, goal):
    path = [goal]
    c_parent = smGraph[goal].parent
    while c_parent != None:
        path.append(c_parent)
        c_parent = smGraph[c_parent].parent

    path.reverse()
    return path
        

print("Path by DFS is : ", DFS(graphC, 'A', 'K'))
