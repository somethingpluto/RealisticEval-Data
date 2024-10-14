public class Tester {

    private Graph graph;

    @Before
    public void setUp() {
        // Initialize the graph here if needed
    }

    @Test
    public void testEmptyGraph() {
        Graph g = new Graph(new ArrayList<>());
        Map<Integer, List<Graph>> expected = new HashMap<>();
        assertEquals(expected, g.cyclesBySize(),
                     "Failed: Expected an empty map for an empty graph.");
    }

    @Test
    public void testGraphNoCycles() {
        List<List<String>> edges = Arrays.asList(
                Arrays.asList("1", "2"),
                Arrays.asList("2", "3")
        );
        Graph g = new Graph(edges);
        Map<Integer, List<Graph>> expected = new HashMap<>();
        assertEquals(expected, g.cyclesBySize(),
                     "Failed: Expected an empty map for a graph with no cycles.");
    }

    @Test
    public void testSimpleCycles() {
        List<List<String>> edges = Arrays.asList(
                Arrays.asList("1", "2"),
                Arrays.asList("2", "3"),
                Arrays.asList("3", "1")
        );
        Graph g = new Graph(edges);
        Map<Integer, List<Graph>> results = g.cyclesBySize();
        assertEquals(1, results.get(3).size(),
                     "Failed: Expected one cycle of length 3.");
        List<String> cycleNodes = results.get(3).get(0).getGraph().vertexSet().stream()
                                         .sorted()
                                         .collect(Collectors.toList());
        assertEquals(Arrays.asList("1", "2", "3"), cycleNodes,
                     "Failed: Expected cycle nodes to match.");
    }

    @Test
    public void testMultipleCycles() {
        List<List<String>> edges = Arrays.asList(
                Arrays.asList("1", "2"),
                Arrays.asList("2", "3"),
                Arrays.asList("3", "1"),
                Arrays.asList("3", "4"),
                Arrays.asList("4", "1")
        );
        Graph g = new Graph(edges);
        Map<Integer, List<Graph>> results = g.cyclesBySize();
        assertEquals(1, results.get(3).size(),
                     "Failed: Expected one cycle of length 3.");
        assertEquals(1, results.get(4).size(),
                     "Failed: Expected one cycle of length 4.");
    }
}