from importlib.resources import path

import data_fetcher

def greedy(graph, locationData, start, goal):#Greedy Best First Search

    expanded_nodes= [start]
    traversalCost=0
    visited=set()

    goalCords=(locationData.get(goal,None)["lat"],locationData.get(goal,None)["lon"])#We will be using the latitude and longitude of the cities as a heuristic to determine which city is closest to the goal
    #goalCords now reformed as a tuple of (lat,lon)
    queue=[(data_fetcher.haversine_distance((locationData.get(start,None)["lat"], locationData.get(start,None)["lon"]), goalCords), start, [start])]

    while queue:#Continues till the queue is empty
        queue.sort(key=lambda x:x[0])#Puts the closest city as the next city to be explored without thinking of edge cost

        CurrentDistance,CurrentLocation,path=queue.pop(0)

        if CurrentLocation==goal:
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]
                return path,traversalCost,expanded_nodes

        for neighborLocation in graph.get(CurrentLocation,{}):
            if neighborLocation not in visited:

                visited.add(neighborLocation)#Adding Stuff to lists
                expanded_nodes.append(neighborLocation)

                neighborCords=(locationData.get(neighborLocation,None)["lat"],locationData.get(neighborLocation,None)["lon"])
                queue.append((data_fetcher.haversine_distance(neighborCords,goalCords),neighborLocation,path+[neighborLocation]))#Add the distance to the next city when appending queue a new city

    return None, 0, []

def astar(graph, locationData, start, goal):#A* Search

    expanded_nodes= [start]
    traversalCost=0
    visited=set()

    goalCords=(locationData.get(goal,None)["lat"],locationData.get(goal,None)["lon"])

    queue=[(data_fetcher.haversine_distance((locationData.get(start,None)["lat"], locationData.get(start,None)["lon"]), goalCords), 0, start, [start])]
            #(Distance to Goal, PathCost, CurrentLocation,Path)=tuple - All of these values describe the above array of tuples

    while queue:#Continue till the queue is empty
        queue.sort(key=lambda x:x[0]+x[1])#adds the distance to goal and path cost as a heuristic to determine which city to go to next
        #The Lower the value, the better as we will be closer to the goal without having to high of a path cost


        CurrentDistance,PathCost,CurrentLocation,path=queue.pop(0)

        if CurrentLocation==goal:
            for i in range(len(path)-1):
                traversalCost+=graph[path[i]][path[i+1]]
                return path,traversalCost,expanded_nodes
    
            for neighborLocation in graph.get(CurrentLocation,{}):
                if neighborLocation not in visited:
    
                    visited.add(neighborLocation)#Adding Stuff to lists
                    expanded_nodes.append(neighborLocation)
    
                    neighborCords=(locationData.get(neighborLocation,None)["lat"],locationData.get(neighborLocation,None)["lon"])
                    distanceToGoal=data_fetcher.haversine_distance(neighborCords,goalCords)
                    newPathCost=PathCost+graph[CurrentLocation][neighborLocation]

                    queue.append((distanceToGoal,newPathCost,neighborLocation,path+[neighborLocation]))#Add the distance to the next city when appending queue a new city



 
    
    return None, 0, []

