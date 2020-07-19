
# A Node, represented as a single cell in a grid, with edges representing
# directional neighbors based on index in edge array
class Node:
    def __init__(self,position):
        self.pos = position;
        # indices represent up,down,left,and right neighbors respectively
        self.edges = [None, None, None, None]
        self.color = "white"


    # Set a connection between this node and a neighbor represented by a
    # given edge to its respective direction represented by the given index.
    def connect(self,edge, index):

        self.edges[index] = edge;

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
