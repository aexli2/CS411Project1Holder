import os
import json
from flask import Flask, render_template, jsonify, request
from uninformed import dfs,bfs,ucs,ids
from informed import astar,greedy

app = Flask(__name__)

MAP_DATA_FILE = "map_data.json"


def load_map_data():
    """Load graph and location data from map_data.json if available."""
    if os.path.exists(MAP_DATA_FILE):
        try:
            with open(MAP_DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {MAP_DATA_FILE}: {e}")
    return {
        "region": "State / Metro Area",
        "total_cities": 0,
        "total_edges": 0,
        "locations": {},
        "graph": {}
    }


@app.route("/")
def index():
    """Renders the main deployment webpage."""
    return render_template("index.html")


@app.route("/api/map", methods=["GET"])
def get_map():
    """Returns map locations and graph connections."""
    data = load_map_data()
    return jsonify(data)


@app.route("/api/search", methods=["POST"])
def search():
    """
    Search endpoint placeholder for deployment testing.
    """
    
    graph = load_map_data().get("graph",{})#Load data from JSON file and atatch it to graph



    #Prebuilt
    payload = request.get_json() or {}
    start = payload.get("start", "")
    goal = payload.get("goal", "")
    algorithm = payload.get("algorithm", "")


    #If list of algorithims
    if algorithm=="bfs":
        path,cost,expanded_nodes = bfs(graph,start,goal)
    elif algorithm=="dfs":
        path,cost,expanded_nodes = dfs(graph,start,goal)
    elif algorithm=="ucs":
        path,cost,expanded_nodes = ucs(graph,start,goal)
    elif algorithm=="ids":
        path,cost,expanded_nodes = ids(graph,start,goal)
    elif algorithm=="greedy":
        path,cost,expanded_nodes = greedy(graph,start,goal)
    elif algorithm=="astar":
        path,cost,expanded_nodes = astar(graph,start,goal)
    else:
        path=None
        cost=0
        expanded_nodes=0


    return jsonify({
        "status": "ready",
        "message": f"Deployment server active. Request received for algorithm '{algorithm}' from '{start}' to '{goal}'.",
        "path": path,
        "cost": cost,
        "nodes_expanded": expanded_nodes
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
