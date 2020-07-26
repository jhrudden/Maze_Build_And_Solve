
# A Node, represented as a single cell in a grid, with edges representing
# directional neighbors based on index in edge array
class Node:
    def __init__(self,position):
        self.pos = position;
        # indices represent up,down,left,and right neighbors respectively
        self.edges = [None, None, None, None]
        self.color = "white"


    # Set a connection between this node and a neighbor represented by a
    # given edge to its respective direction represented by the given node's pos
    def connect(self,edge, to_node):

        # is this node on the same level as the other given node
        if self.pos[0] == to_node.pos[0]:
            # is the to_node to the left of this node
            if self.pos[1] > to_node.pos[1]:
                self.edges[2] = edge;

            # the to_node must be to the right
            else:
                self.edges[3] = edge;
        else:
            # is the to_node above  this node
            if self.pos[0] > to_node.pos[0]:
                self.edges[0] = edge;

            # must be below
            else:
                self.edges[1] = edge;


    # Output a string representing a Cell with walls representing Null
    # entries in an edge array.
    def draw_cell(self):
        string = "";
        if self.edges[2] is None:
            string += "|";
        else:
            string += " ";

        if self.edges[1] is None:
            string += "_";
        else:
            string += " ";
        return string


    def print_edges(self):
        string = [self.pos]
        if not self.edges[0] is None:
            string.append("up")
        if not self.edges[1] is None:
            string.append("down")
        if not self.edges[2] is None:
            string.append("left")
        if not self.edges[3] is None:
            string.append("right")

        return string
