function topologicalSortDFS(vertices, edges) {
    // Create adjacency list for the graph
    let adjList = new Array(vertices.length).fill(null).map(() => []);
    for(let [src, dest] of edges){
        adjList[src].push(dest);
    }

    // Initialize visited array
    let visited = new Array(vertices.length).fill(false);

    // Stack to store the result
    let stack = [];

    // Recursive function to perform DFS
    function dfs(vertex) {
        if(visited[vertex]){
            return false; // Cycle detected
        }
        visited[vertex] = true;

        for(let neighbor of adjList[vertex]){
            if(!dfs(neighbor)){
                return false; // Cycle detected
            }
        }

        stack.push(vertex);
        return true;
    }

    // Perform DFS for all unvisited nodes
    for(let i=0; i<vertices.length; i++){
        if(!visited[i]){
            if(!dfs(i)){
                return []; // Graph has a cycle
            }
        }
    }

    // Return the result in reverse order
    return stack.reverse();
}
