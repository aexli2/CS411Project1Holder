# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.
---

## Student Information 
- **Name:** Aaron Exline
- **UID (netID):** aexli2
- **UIN:** 660619880

---

## Section 1: Selected City Region
- **Selected Region:** Illinois

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 35
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://cs411project1holder.onrender.com/
- **Video Presentation Link:** https://drive.google.com/file/d/16VGddnRosj5oJAuZFG98tm2jdwwNCgbQ/view

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    In my opinion, the best algorithim to use for the route finding problem would be the A* Algorithim. This algorithim uses takes into account the heuristic and cost of each path to try to find the best and closest path before going to the next node. It also only takes the path that is most efficient in terms of going directly towards the goal location without taking any other paths that may end up costing it more time like with ucs which explores all shortest route options. Greedy doesn't take into account path cost so there is a high chance that it will return a high costing path towards the goal location. ids takes a long time to search for the goal location as it keeps revisitng the same locations it has already compared. bfs checks visits and checks every path making it no efficient for searching. dfs plan and simple visits the deepest node and comes up which costs a lot in runtime if the city graph extends across the entire United States of America. All in all, A* is efficient and the best for this problem in my opinion as it expands only towards cities thus costing low in search time and only takes the path which will get it closest and with the least cost to the goal location as possible causing it to also be low in path cost.
- **Search Efficiency (Nodes visited/time taken comparison):**
    A* is the best in regards to being efficient and optimal in regards to path cost same as ucs. A* and ucs both look for the least costing path but what seperates them is their expansion method. ucs will try not reach towards the goal city but towards the least costing path so it will be visiting every least costing path it comes across towards others paths thus costing a lot in runtime making it not that good in search efficiency. A* uses a heuristic to visit and compare cities which is only on the path towards the goal city causing it's runtime and search cost to lower as a result from it not having to visit and compare all other paths. Greedy costs less for computation time and immediately visit towards the goal city by using the shortest path making it very efficient in term searching and reaching the goal in the fastest time but it doesn't take into account path cost. Greedy is the fastest in terms of search but the path cost doesn't make it reliable. dfs is a very expensive algorithm as in they traverse and visit to the very bottom of the list and comparing every city within every path and up thus costing a lot in search time just to go to the bottom of the list making dfs not an efficient search algorithm as it will end up costing alot of runtime. bfs is also not an efficient search algorithm in terms of search efficiency. bfs will visit very node in the list starting from the shallowest neighbor and slowly visit every node and compare every city until it has reached the goal state costing so much runtime during the search making it very uneficient. ids uses both bfs and dfs in terms of visiting different nodes as it searches through each depth starting from the starting city until it reaches the goal city. It keep revisiting every node single node in this though and is in a constant state of searching and recomparing every city thus costing a lot in runtime making ids algorthm despite adapting both stategies not an efficient search algorthm.
- **Link the idea of search algorithm to today Generative AI.** 
    Search algorithms is integrated into some modern generative AI. Generative AI uses a data base of information which it can freely pick information from and browse to collect more information from online sources. Lets say however that you want it to generate a comedic news article for instance, it will use a search algorithm to navigate it's data base and have it run on a heuristic let's say for this own being news related information and comedy. It will take the quickest path through it's data base to collect that information, avoiding paths that are not relevant to the heuristic we have given it thus allowing it to traverse quicker through it's data base to grab all relevant information. After that is done it will compile all that information it has gathered from it's search path and output a funny news article for the user to read. If it wasn't using a search algorithm and instead a linked list, it would take forever to reach and gather the speciifc information we have requested from the countless amounts of information it has stored within it's database. So all in all, if the modern day generative AI didn't use a informed search algorithm it wouldn't have been as efficient as it would have needed to be. 

