
def bfs(graph, start, goal):
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
            
        
            
            





    return None,0,0

def dfs(graph, start, goal):
    return None,0,0

def ucs(graph, start, goal):
    return None,0,0

def ids(graph, start, goal):
    return None,0,0