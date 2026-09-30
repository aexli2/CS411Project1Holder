
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
    farthestDepth=False

    if(start==goal):
        return ([start,goal],0,1)


    while queue:
        
        queue.sort(key=lambda x: x[0],reverse=True)
        pathCost,currentLocation,path= queue.pop(0)

        

        if(currentLocation in visited):
            continue

        expanded_nodes.append(currentLocation)

        visited.add(currentLocation)

        #print(path)
        #print(pathCost)
        #print(expanded_nodes)

        if currentLocation == goal:
            
            return path,pathCost,expanded_nodes

        for neighborLocation in graph[currentLocation]:#Sorts based upon the farthest depth
            #print(neighborLocation)
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted 
                visited.add(neighborLocation)

                newPathCost=pathCost+graph[currentLocation][neighborLocation]

                queue.append(newPathCost,neighborLocation,path+[neighborLocation])

    return None, 0, []

""""
    while farthestDepth==False:#Continues till we reach the farthest depth
        queue.sort(key=lambda x: x[0],reverse=True)#Sorts so that the first grabbed path is going to be the farthest
        farthestDepth=True
        pathCost,currentLocation,path=queue.pop()#Grabs the last location in the queue and add it to the path
        visited.add(currentLocation)

        for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x], reverse=True):#Sorts based upon the farthest depth
            if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted 

                farthestDepth=False
                visited.add(neighborLocation)

                newPathCost= pathCost + graph[currentLocation][neighborLocation]

                queue.append((newPathCost,neighborLocation,path+[neighborLocation]))

        if(farthestDepth==True):
            queue.append((pathCost,currentLocation,path))

    while queue:
        queue.sort(key=lambda x: x[0],reverse=True)#Sorts the queue so that the we are at the deepest depth city/location
        pathCost,currentLocation,path=queue.pop()#Grabs the last location in the queue and add it to the path
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:
            return path,pathCost,expanded_nodes

        print(currentLocation)
        print(path)
        newPathCost= pathCost - graph[path[-2]][currentLocation]
        path=path[:-1]
        queue.append((newPathCost,path[-1],path))

    

        """


   

def ucs(graph, start, goal):# Uniform Cost Search


    expanded_nodes= []
    visited=set()
    queue=[(0,start,[start])]#queue is a list of tuples, each tuple contains the cost, current location, and path taken to reach that location

    while queue:#Continues till the queue is empty
        queue.sort(key=lambda x: x[0])#Sorts upon path cost which is stored in the first stored value in the tuple at index [0], Integral for UCS search to work properly
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

    while queue:#Continues till the queue is empty
        queue=sorted(queue,key= lambda x:queue[x][0], reverse=True)#Sorts by using the 

        pathCost,currentLocation,path=queue.pop()#Grabs the last location in the qeue and add it to the path
        visited.add(start)
        expanded_nodes.append(currentLocation)

        if currentLocation==goal:#If the Current Location is the goal, iterate through path and grabs the cost
            return path,pathCost,expanded_nodes

        if len(path)<=locationDepth:#will continue to search for goal if the path is less than or equal to the current depth, if not it will continue to the next iteration of the search
            for neighborLocation in sorted(graph.get(currentLocation,{}), key=lambda x: graph[currentLocation][x], reverse=True):#Browse the neighboring locations of the current Location
                if neighborLocation not in visited:#If that location is yet to be recorded inside of Visisted

                    visited.add(neighborLocation)
                    newPathCost= pathCost+ graph[currentLocation][neighborLocation]
                    queue.append((neighborLocation,path+[neighborLocation]))

        if not queue:#If the queue is empty,Reset the stats and increase the depth for the next iteration
            queue=[(start,[start])]
            visited.clear()
            
            locationDepth+=1#Preparing for the next iteration

    return None,0,[]