function getMidsFromEdges(edges) {
    edges = Array.from(edges);

    // Calculate midpoints using array operations
    const mids = edges.slice(0, -1).map((edge, index) => {
        return (edge + edges[index + 1]) / 2;
    });

    return mids;
}