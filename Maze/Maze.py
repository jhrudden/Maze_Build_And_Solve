import random as rand
from Edge import Edge
from Node import Node

class Maze:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows;
        self.num_cols = num_cols;
        self.grid = None;

        self.init_grid();

        # Construct the grid of Nodes, which will later be turned into a Maze
    def init_grid(self):
        grid = [];
        area = self.num_cols * self.num_rows

        # contruct a rows and cols of a blank grid
        for row in range(self.num_rows):
            curr_row = []
            for col in range(self.num_cols):
                curr_node = Node((row,col));
                curr_row.append(curr_node)

                # Once a node has been constructed connect it and the Node above
                # to eachother if possible
                # also give edges weights for future use
                # is there an up neighbor?
                if row > 0:
                    up_neighbor = grid[row-1][col]
                    edge_1 = Edge(curr_node, up_neighbor, rand.randrange(area))
                    curr_node.connect(edge_1,0)
                    edge_2 = Edge(up_neighbor, curr_node, rand.randrange(area))
                    up_neighbor.connect(edge_2,1)
                # is there a left neighbor?

                if col > 0:
                    left_neighbor = curr_row[col-1]
                    edge_1 = Edge(curr_node, left_neighbor, rand.randrange(area))
                    curr_node.connect(edge_1,2);
                    edge_2 = Edge(left_neighbor, curr_node, rand.randrange(area))
                    left_neighbor.connect(edge_2,3)
            # once every col of a row has been constructed the row is complete
            grid.append(curr_row);

        # grid is now complete and all cells have been connected by edges
        # to their respective neighbors
        self.grid = grid

    def kruskel(self):



    # return a string representing the currently constructed Maze
    def draw_grid(self):
        print(" _" * self.num_cols);
        for row in range(self.num_rows):
            curr_row_string = "|"
            for col in range(self.num_cols):
                curr_node_drawing = self.grid[row][col].draw_cell()
                if col == 0:
                    curr_node_drawing = curr_node_drawing[1:]
                curr_row_string += curr_node_drawing

            curr_row_string += "|"
            print(curr_row_string)

grid = Maze(10,10)
grid.draw_grid()