

class Edge:
    def __init__(self, from_node,  to_node, weight):
        self.to_node = to_node;
        self.from_node = from_node;
        self.weight = weight;

    def compare(self, other_edge):
        return self.weight - other_edge.weight;
