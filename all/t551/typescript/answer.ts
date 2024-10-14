function getMidsFromEdges(edges: number[]): number[] {
    const edgeArray = edges;

    // Calculate midpoints using array operations
    const mids = edgeArray.slice(0, -1).map((edge, index) => {
        return (edge + edgeArray[index + 1]) / 2;
    });

    return mids;
}