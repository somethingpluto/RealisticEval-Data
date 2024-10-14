const { Graph } = require('graphology');

class Graph {
  constructor(edges) {
    this.graph = new Graph({ type: 'directed' });
    edges.forEach(([source, target]) => {
      this.graph.addEdge(source, target);
    });
  }

  cyclesBySize(filterRepeatNodes = true) {
    const allCycles = this.findAllSimpleCycles();
    const cycles = allCycles.filter(cycle => cycle.length > 2);

    if (filterRepeatNodes) {
      cycles.filter(cycle => new Set(cycle).size === cycle.length);
    }

    const uniqueCycles = Array.from(new Set(cycles.map(cycle => JSON.stringify(cycle)))).map(strCycle => JSON.parse(strCycle));
    const uniqueCyclesBySize = {};

    uniqueCycles.forEach(cycle => {
      const size = cycle.length;
      if (!uniqueCyclesBySize[size]) {
        uniqueCyclesBySize[size] = [];
      }
      uniqueCyclesBySize[size].push(this.graph.subgraph(cycle));
    });

    return uniqueCyclesBySize;
  }

  findAllSimpleCycles() {
    const cycles = [];
    const stack = [];
    const onCycle = cycle => cycles.push(cycle);
    this.graph.forEachNode(node => {
      this.graph.forEachOutgoingEdge(node, edge => {
        const target = this.graph.getOpposite(node, edge);
        if (!stack.includes(target)) {
          stack.push(target);
          this.graph.traverseSimplePaths(node, target, onCycle);
          stack.pop();
        }
      });
    });
    return cycles;
  }
}