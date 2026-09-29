
def bfs(graph, start, goal):#Breadth First Search

    expanded_nodes=[start]
    visited = set()
    traversalCost=0
    queue = [(start,[start])]

    while queue:#Continues till the queue is empty
        currentLocation,path=queue.pop(0)#Grabs the first location in the queue and add it to the path

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
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
    queue=[(0,start,[start])]#Pretty much ucs without the sorting of the queue, which is what makes it depth first search

    while queue:#Continues till the queue is empty
        currentCost, currentLocation, path = queue.pop()#Grabs the last location in the queue and add it to the path

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]

            return path,traversalCost,expanded_nodes


        for neighborLocation in graph.get(currentLocation,{}):#Browse the neighboring locations of the current Location
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                visited.add(neighborLocation)
                expanded_nodes.append(neighborLocation)

                newCost=currentCost+graph[currentLocation][neighborLocation]#Updates the cost the path is going to take to reach the next location, which is hopefully going to be the goal
                queue.append((newCost,neighborLocation,path+[neighborLocation]))

    return None,0,[]

def ucs(graph, start, goal):# Uniform Cost Search


    expanded_nodes= [start]
    traversalCost=0
    visited=set()
    queue=[(0,start,[start])]#queue is a list of tuples, each tuple contains the cost, current location, and path taken to reach that location

    while queue:#Continues till the queue is empty
        queue.sort(key=lambda x: x[0])#Sorts upon path cost which is stored in the first stored value in the tuple at index [0], Integral for UCS search to work properly
        currentCost, currentLocation, path = queue.pop(0)#Cost is recorded inside of the queue which is important for tracking what goes first which is what the sort is for

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]

            return path,traversalCost,expanded_nodes


        for neighborLocation in graph.get(currentLocation,{}):#Browse the neighboring locations of the current Location
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                visited.add(neighborLocation)
                expanded_nodes.append(neighborLocation)

                newCost=currentCost+graph[currentLocation][neighborLocation]#Updates the cost the path is going to take to reach the next location, which is hopefully going to be the goal
                queue.append((newCost,neighborLocation,path+[neighborLocation]))



    return None,0,[]

def ids(graph, start, goal):# Iterative Depth Search

    expanded_nodes= [start]
    traversalCost=0
    visited=set()
    queue=[(start,[start])]

    locationDepth=0#Tracks depth for each iteration of the search

    while queue:#Continues till the queue is empty
        currentLocation,path=queue.pop()#Grabs the last location in the qeue and add it to the path

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]

            return path,traversalCost,expanded_nodes

        if len(path)<=locationDepth:#will continue to search for goal if the path is less than or equal to the current depth, if not it will continue to the next iteration of the search
            for neighborLocation in graph.get(currentLocation,{}):#Browse the neighboring locations of the current Location
                if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                    visited.add(neighborLocation)
                    expanded_nodes.append(neighborLocation)
                    queue.append((neighborLocation,path+[neighborLocation]))

        if not queue:#If the queue is empty,Reset the stats and increase the depth for the next iteration
            queue=[(start,[start])]
            visited.clear()
            expanded_nodes=[start]
            locationDepth+=1#Preparing for the next iteration

        
    
    return None,0,[]