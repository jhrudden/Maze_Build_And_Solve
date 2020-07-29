

class Edge:
    def __init__(self, from_node,  to_node, weight):
        self.to_node = to_node;
        self.from_node = from_node;
        self.weight = weight;

    def compare(self, other_edge):
        return self.weight - other_edge.weight;

    def connect(self):
        self.from_node.connect(self, self.to_node);
        reverse = self.reverse_edge();
        self.to_node.connect(reverse, self.from_node);

    def reverse_edge(self):
        return Edge(self.to_node, self.from_node, self.weight);

    # Are both the to and from nodes apart of same subset of a graph?
    def is_loop(self, dictionary):

        to_subset = dictionary.get(self.to_node)
        from_subset = dictionary.get(self.from_node)
        while to_subset != dictionary.get(to_subset):
            to_subset = dictionary.get(to_subset)
        while from_subset != dictionary.get(from_subset):
            from_subset = dictionary.get(from_subset)

        if not to_subset is None and not from_subset is None:
            return dictionary.get(from_subset) == dictionary.get(to_subset);

        return False;

    def add_to_subset(self, dictionary):
        to_subset = dictionary.get(self.to_node)
        from_subset = dictionary.get(self.from_node)
        if to_subset is None and from_subset is None:
            # create a head node to a subset of graph
            dictionary.update({self.from_node:self.from_node})
            # label the incident node as part of this new made subset
            dictionary.update({self.to_node:self.from_node})

        elif to_subset is None:
            # label the incident node as connected to the from_node's head node
            dictionary.update({self.to_node:self.from_node})

        elif from_subset is None:
            # label the start node as connected to the to_node's head node
            dictionary.update({self.from_node:self.to_node})

        else:
            while to_subset != dictionary.get(to_subset):
                to_subset = dictionary.get(to_subset)
            while from_subset != dictionary.get(from_subset):
                from_subset = dictionary.get(from_subset)
            dictionary.pop(to_subset)
            dictionary.update({to_subset: from_subset})


    # gross getter
    def find_incident(self):
        return self.to_node;
