
def bfs(graph, start, goal):#Breadth First Search

    expanded_nodes=[start]
    visited = set()
    traversalCost=0
    queue = [(start,[start])]

    while queue:#Continues till the queue is empty
        currentLocation,path=queue.pop(0)#Grabs the first location in the queue and add it to the path

        if currentLocation==goal:#If the Current Location is the goal, iterate through path the grabs the cost
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]

            return path,traversalCost,expanded_nodes

        
        for neighborLocation in graph.get(currentLocation,{}):
            if neighborLocation not in visited:
                visited.add(neighborLocation)
                expanded_nodes.append(neighborLocation)
                queue.append((neighborLocation,path+[neighborLocation]))


    return None,0,[]

def dfs(graph, start, goal):#Depth First Search

    expanded_nodes= [start]
    traversalCost=0
    visited=set()
    queue=[(0,start,[start])]
    while queue:#Continues till the queue is empty
        break

    return None,0,[]

def ucs(graph, start, goal):# Uniform Cost Search


    expanded_nodes= [start]
    traversalCost=0
    visited=set()
    queue=[(0,start,[start])]#queue is a list of tuples, each tuple contains the cost, current location, and path taken to reach that location

    while queue:#Continues till the queue is empty
        queue.sort(key=lambda x: x[0])#Sorts upon path cost which is stored in the first stored value in the tuple at index [0]
        currentCost, currentLocation, path = queue.pop(0)#Cost is recorded inside of the queue which is important for tracking what goes first which is what the sort is for
        break


    return None,0,[]

def ids(graph, start, goal):# Iterative Depth Search

    expanded_nodes= [start]
    traversalCost=0
    visited=set()
    queue=[(0,start,[start])]

    while queue:#Continues till the queue is empty
        break
    
    return None,0,[]