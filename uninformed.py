
def bfs(graph, start, goal):#Breadth First Search

    expanded_nodes=[]
    visited = set()
    
    queue = [(0,start,[start])]

    while queue:#Continues till the queue is empty

        pathCost,currentLocation,path=queue.pop(0)#Grabs the first location in the queue and add it to the path
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
    
            return path,pathCost,expanded_nodes

        
        for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x]):#Sorts neighbor Locations to have the first one be the shallowest
            if neighborLocation not in visited:
                visited.add(neighborLocation)

                newPathCost=pathCost+graph[currentLocation][neighborLocation]
                queue.append((newPathCost,neighborLocation,path+[neighborLocation]))


    return None,0,[]

def dfs(graph, start, goal):#Depth First Search

    expanded_nodes= []
    visited=set()
    queue=[(0,start,[start])]#Pretty much ucs without the sorting of the queue, which is what makes it depth first search
    

    if(start==goal):
        return ([start,goal],0,1)

    #The first pop of the queue should be at the deepest depth
    #Must populate the queue with the deepest depth first, then pop the next deepest depth and continue on in that fashion
    while queue:#Continues till the queue is empty

        pathCost,currentLocation,path=queue.pop()#Grabs the last location in the queue and add it to the path which is the deepest depth within the queue
        visited.add(start)
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
    
            return path,pathCost,expanded_nodes

        for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x], reverse=True):#Browse the neighboring locations of the current Location
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                visited.add(neighborLocation)
                newPathCost=pathCost+graph[currentLocation][neighborLocation]
                queue.append((newPathCost,neighborLocation,path+[neighborLocation]))



        
        

    return None, 0, []



   

def ucs(graph, start, goal):# Uniform Cost Search


    expanded_nodes= []
    visited=set()
    queue=[(0,start,[start])]#queue is a list of tuples, each tuple contains the cost, current location, and path taken to reach that location

    while queue:#Continues till the queue is empty
        queue.sort(key=lambda x: x[0])#Sorts upon path cost which is stored in the first stored value in the tuple at index [0], mimics a priority queue
        currentCost,currentLocation,path=queue.pop(0)#Cost is recorded inside of the queue which is important for tracking what goes first which is what the sort is for
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
    
            return path,currentCost,expanded_nodes


        for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x]):#Browse the neighboring locations of the current Location and sort them by shortest distance
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                visited.add(neighborLocation)

                newCost=currentCost+graph[currentLocation][neighborLocation]#Updates the cost the path is going to take to reach the next location, which is hopefully going to be the goal
                queue.append((newCost,neighborLocation,path+[neighborLocation]))

    return None,0,[]

def ids(graph, start, goal):# Iterative Depth Search

    expanded_nodes= []
    visited=set()
    queue=[(0, start,[start])]

    locationDepth=0#Tracks depth for each iteration of the search

    #Does the same thing as DFS, but must keep track of the depth of the search
    #I have to make sure that the search is not going to go deeper than the current depth: what the (if len(path)) section is for

    if (start==goal):
        return ([start,goal],0,1)


    while queue:#Continues till the queue is empty
    
        pathCost,currentLocation,path=queue.pop()#Grabs the last location in the queue and add it to the path which is the deepest depth within the queue
        visited.add(start)
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
            return path,pathCost,expanded_nodes

        if len(path)<locationDepth:#Iterates through the neighboring locations of the current location and adds them to the queue if they are not already visited
            for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x], reverse=True):#Browse the neighboring locations of the current Location
                if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                    visited.add(neighborLocation)
                    newPathCost=pathCost+graph[currentLocation][neighborLocation]
                    queue.append((newPathCost,neighborLocation,path+[neighborLocation]))

        if len(queue)==0:#If the queue is empty then restart
            locationDepth+=1
            queue=[(0, start,[start])]
            visited=set()

    return None,0,[]