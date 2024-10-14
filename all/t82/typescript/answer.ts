import * as _ from 'lodash';
import { DiGraph } from 'networkx';

interface Edge {
  source: any;
  target: any;
}

class Graph {
  private graph: DiGraph;

  constructor(edges: Edge[]) {
    this.graph = new DiGraph();
    edges.forEach(edge => {
      this.graph.addEdge(edge.source, edge.target);
    });
  }

  public cyclesBySize(filterRepeatNodes: boolean = true): Record<any, DiGraph[]> {
    const allCycles = Array.from(this.graph.simpleCycles());
    const cycles = allCycles.filter(cycle => cycle.length > 2);

    if (filterRepeatNodes) {
      cycles.filter(cycle => _.uniq(cycle).length === cycle.length);
    }

    const uniqueCycles = _.uniq(cycles.map(cycle => _.sortBy(_.uniq(cycle))));
    const uniqueCyclesBySize: Record<any, DiGraph[]> = {};

    uniqueCycles.forEach(cycle => {
      const size = cycle.length;
      const subgraph = this.graph.subgraph(cycle);
      if (!uniqueCyclesBySize[size]) {
        uniqueCyclesBySize[size] = [];
      }
      uniqueCyclesBySize[size].push(subgraph);
    });

    return uniqueCyclesBySize;
  }
}