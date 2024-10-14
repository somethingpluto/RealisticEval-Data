describe('TestGraphCycles', () => {
  it('test_empty_graph', () => {
    const g = new Graph([]);
    expect(g.cyclesBySize()).toEqual({});
    expect(g.cyclesBySize()).toStrictEqual({});
  });

  it('test_graph_no_cycles', () => {
    const g = new Graph([[1, 2], [2, 3]]);
    expect(g.cyclesBySize()).toEqual({});
    expect(g.cyclesBySize()).toStrictEqual({});
  });

  it('test_simple_cycles', () => {
    const g = new Graph([[1, 2], [2, 3], [3, 1]]);
    const results = g.cyclesBySize();
    expect(Object.keys(results).length).toBe(1);
    expect(results[3]).toHaveLength(1);
    expect(results[3][0].nodes()).toEqual([1, 2, 3]);
  });

  it('test_multiple_cycles', () => {
    const g = new Graph([[1, 2], [2, 3], [3, 1], [3, 4], [4, 1]]);
    const results = g.cyclesBySize();
    expect(Object.keys(results).length).toBe(2);
    expect(results[3]).toHaveLength(1);
    expect(results[4]).toHaveLength(1);
  });
});