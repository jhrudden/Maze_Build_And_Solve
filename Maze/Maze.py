import random as rand
from Edge import Edge
from Node import Node
from DataStructures.PriorityQ import PriorityQ

class Maze:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows;
        self.num_cols = num_cols;
        self.grid = None;

        self.init_grid();

        # Construct the grid of Nodes, which will later be turned into a Maze
    def init_grid(self):
        grid = [];

        # contruct a rows and cols of a blank grid
        for row in range(self.num_rows):
            curr_row = []
            for col in range(self.num_cols):
                curr_node = Node((row,col));
                curr_row.append(curr_node)


            # once every col of a row has been constructed the row is complete
            grid.append(curr_row);

        # grid is now complete and all cells have been connected by edges
        # to their respective neighbors
        self.grid = grid

    def kruskel(self):
        priority = self.init_edge_list()
        graph_subsets = dict()

        # continue to extract edges from the priority queue untill it is empty
        while not priority.is_empty():
            # grab the current priority edge from the queue
            min = priority.remove_min();

            if not min.is_loop(graph_subsets):

                min.add_to_subset(graph_subsets);
                min.connect();

    # initialize a priority queue with mock edges for every possible connection
    # in this grid between nodes, all with random wieghts
    def init_edge_list(self):
        area = self.num_cols*self.num_rows
        priority = PriorityQ();

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                curr_node = self.grid[row][col]

                # if possible create a mock edge between current node add
                # node above
                if row > 0:
                    up_neighbor = self.grid[row-1][col]
                    edge_1 = Edge(curr_node, up_neighbor, rand.randrange(area))
                    edge_2 = Edge(up_neighbor, curr_node, rand.randrange(area))
                    priority.insert(edge_1)
                    priority.insert(edge_2)

                # if possible create a mock edge between current node add
                # node to the right
                if col > 0:
                    left_neighbor = self.grid[row][col-1]
                    edge_1 = Edge(curr_node,left_neighbor,rand.randrange(area))
                    edge_2 = Edge(left_neighbor,curr_node, rand.randrange(area))
                    priority.insert(edge_1)
                    priority.insert(edge_2)

        return priority;


    # # TODO: if neighbors already are in dictionary don't add them to work list
    # or to dict again
    def prims(self):
        vertices = [];
        total_vertices = self.num_cols * self.num_rows;

        # setup
        node_index = random.randrange(total_vertices);
        row_index = (node_index // self.num_cols) - 1
        col_index = (node_index - ((row_index) * self.num_cols)) - 1

        first_node = self.grid[row_index][col_index]

        work_list = [first_node]

        connected_to = dict()

        while len(vertices) < total_vertices:
            current_node = work_list.pop(random.randrange(len(work_list)))
            vertices.append(current_node)
            [curr_row, curr_col] = current_node.pos;


            if curr_col >= 0 and curr_col < self.num_cols - 1:
                right_neighbor = self.grid[curr_row][curr_col+1]
                work_list.append(right_neighbor);
                connected_to.update({right_neighbor : current_node})

            if curr_col > 0 and curr_col < self.num_cols:
                left_neighbor = self.grid[curr_row][curr_col-1]
                work_list.append(left_neighbor);
                connected_to.update({left_neighbor : current_node})

            if cur_row >= 0 and curr_row < self.num_rows - 1:
                down_neigbor = self.grid[curr_row+1][curr_col]
                work_list.append(down_neigbor);
                connected_to.update({down_neigbor : current_node})

            if cur_row > 0 and curr_row < self.num_rows:
                up_neigbor = self.grid[curr_row-1][curr_col]
                work_list.append(up_neigbor);
                connected_to.update({up_neigbor : current_node})

            connection = connected_to.get(current_node);

            if connection is not None:
                curr_edge = Edge(current_node, connection, 0);
                curr_edge.connect();






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
grid.kruskel()

grid.draw_grid()
