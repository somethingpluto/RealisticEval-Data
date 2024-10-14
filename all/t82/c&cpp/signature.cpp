 std::map<int, std::vector<Graph>> cycles_by_size(bool filter_repeat_nodes = true) const {
        /*
         * Finds all unique cycles in the graph that are larger than size 2, optionally filtering out cycles with repeated nodes.
         *
         * Args:
         *     filter_repeat_nodes (bool): If true, filters out cycles where any node appears more than once.
         *
         * Returns:
         *     std::map<int, std::vector<Graph>>: A map mapping each cycle size to a vector of subgraph objects representing
         *         each unique cycle of that size.
         */
 }