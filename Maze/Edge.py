

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
        return dictionary.get(self.from_node) == dictionary.get(self.to_node);
