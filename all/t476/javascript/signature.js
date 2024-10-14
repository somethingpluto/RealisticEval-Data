/**
 * Achieve topological sorting, based on depth priority search
 *
 * @param {number[]} vertices - A list of vertices in the graph. Each vertex should be a unique integer.
 * @param {Array<Array<number>>} edges - A list of arrays where each array represents a directed edge
 *                                        in the graph and is formed as [startVertex, endVertex].
 *
 * @returns {number[]} A list of vertices in topological order. If the graph contains a cycle,
 *                      and thus cannot have a valid topological ordering, an empty array is returned.
 */
