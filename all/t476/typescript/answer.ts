type Edge = [number, number];
type Graph = Map<number, number[]>;

function topologicalSortDfs(vertices: number[], edges: Edge[]): number[] {
    let adjList: Graph = new Map();
    let visited: boolean[] = Array(vertices.length).fill(false);
    let stack: number[] = [];

    // Build adjacency list representation of the graph
    for(let i=0; i<vertices.length; i++) {
        adjList.set(vertices[i], []);
    }

    for(let edge of edges) {
        adjList.get(edge[0])?.push(edge[1]);
    }

    // Depth first search
    for(let v of vertices) {
        if(!visited[v]) {
            dfs(v);
        }
    }

    // Function to perform DFS
    function dfs(v: number) {
        visited[v] = true;

        for(let neighbor of adjList.get(v)!) {
            if(!visited[neighbor]) {
                dfs(neighbor);
            }
        }

        stack.push(v);
    }

    return stack.reverse();
}