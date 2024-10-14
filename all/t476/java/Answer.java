import java.util.*;

public class Answer {
    public static List<Integer> topologicalSortDFS(List<Integer> vertices, List<List<Integer>> edges) {
        Map<Integer, List<Integer>> adjacencyList = new HashMap<>();
        for(int v : vertices){
            adjacencyList.put(v, new ArrayList<>());
        }
        for(List<Integer> e : edges){
            adjacencyList.get(e.get(0)).add(e.get(1));
        }

        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[vertices.size()];
        for(int i=0; i<visited.length; i++){
            if(!visited[i]){
                dfs(adjacencyList, visited, i, stack);
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!stack.isEmpty()){
            result.add(stack.pop());
        }

        return result;
    }

    private static void dfs(Map<Integer, List<Integer>> adjacencyList, boolean[] visited, int current, Stack<Integer> stack){
        visited[current] = true;
        for(int neighbor : adjacencyList.get(current)){
            if(!visited[neighbor]){
                dfs(adjacencyList, visited, neighbor, stack);
            }
        }
        stack.push(current);
    }
}
