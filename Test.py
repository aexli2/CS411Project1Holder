
from uninformed import dfs

graph = {
    # Your code here
    "connections":{
        "A":[
            {"node":"B","distance":2.0},
            {"node":"C  ","distance":1.0}
        ],
        "B":[
            {"node":"D","distance":2.0},
            {"node":"E","distance":5.0},
        ],
        "C":[
            {"node":"F","distance":2.0},
                ],
        "D":[
            {"node":"G","distance":5.0},
                ],

        "E":[
            {"node":"G","distance":1.0},
                ],

        "F":[
            {"node":"G","distance":4.0},
                ],
        "G":[
            {}
                ]
    }
}

connectionGraph=graph.get("connections",{})

print(dfs(connectionGraph,"A","G"))

