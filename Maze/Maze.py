import random as rand
from Edge import Edge
from Node import Node
from DataStructures.PriorityQ import PriorityQ
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue

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

    # Creates a minimum spanning tree by finding edges with least weight that
    # connects trees in a forest (grid in this case)
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


    # Starting from a random node in a grid add a random neighbor to a maze
    # recursively until all vertices are in the Maze
    def prims(self):
        vertices = [];
        total_vertices = self.num_cols * self.num_rows;
        # setup
        node_index = rand.randrange(total_vertices);
        row_index = ((node_index - 1) // self.num_cols)
        col_index = (node_index - ((row_index) * self.num_cols)) - 1
        print(row_index, col_index)
        # grad the intial node
        first_node = self.grid[row_index][col_index]
        # add it to the nodes to choose to visit at random
        work_list = [first_node]
        # used to determine which node was originally next to any given node,
        # when it is visited
        connected_to = dict()
        # Run untill all vertices have been added to Maze
        while len(vertices) < total_vertices:
            # grab a node at random from seen neighbors list
            current_node = work_list.pop(rand.randrange(len(work_list)))
            vertices.append(current_node)
            [curr_row, curr_col] = current_node.pos;
            # find all the neighbors for this node / nodes directly touching
            # this node, and if they haven't already been seen add them to
            # future nodes to be visited
            if curr_col >= 0 and curr_col < self.num_cols - 1:
                right_neighbor = self.grid[curr_row][curr_col+1]
                if connected_to.get(right_neighbor) is None:
                    work_list.append(right_neighbor);
                    connected_to.update({right_neighbor : current_node})
            if curr_col > 0 and curr_col < self.num_cols:
                left_neighbor = self.grid[curr_row][curr_col-1]
                if connected_to.get(left_neighbor) is None:
                    work_list.append(left_neighbor);
                    connected_to.update({left_neighbor : current_node})
            if curr_row >= 0 and curr_row < self.num_rows - 1:
                down_neigbor = self.grid[curr_row+1][curr_col]
                if connected_to.get(down_neigbor) is None:
                    work_list.append(down_neigbor);
                    connected_to.update({down_neigbor : current_node})
            if curr_row > 0 and curr_row < self.num_rows:
                up_neigbor = self.grid[curr_row-1][curr_col]
                if connected_to.get(up_neigbor) is None:
                    work_list.append(up_neigbor);
                    connected_to.update({up_neigbor : current_node})
            # find the node that was first used to discover this node
            connection = connected_to.get(current_node);
            # connect the current node and the original node that discovered
            # this node as a neighbor in the grid if possible
            if connection is not None:
                curr_edge = Edge(current_node, connection, 0);
                curr_edge.connect();

    # Search for a given node in a depth by depth fashion, only extending, the
    # search to each node neighbor when a wave has been completely searched
    def bfs(self, start_node, end_node):
        return self.find_path(start_node, end_node, Queue())

    # Search for a given node by following a whole branch, then backtracking
    # when a dead end is found
    def dfs(self, start_node, end_node):
        return self.find_path(start_node, end_node, Stack())


    def find_path(self, start_node, end_node, worklist):
        all_paths = dict();
        path_to_sol = []
        # setup
        curr_node = start_node;
        all_paths.update({curr_node:curr_node})

        # When the search block lands on the wanted tile, end the search
        while curr_node != end_node:
            neighbors = curr_node.get_neighbors();
            for neighbor in neighbors:
                if all_paths.get(neighbor) is None:
                    all_paths.update({neighbor : curr_node});
                    worklist.add(neighbor);
            curr_node = worklist.remove();

        # getting path from end to start by pos (start to end)
        while curr_node != start_node:
            path_to_sol.insert(0,curr_node.pos);
            curr_node = all_paths.get(curr_node);
        path_to_sol.insert(0,start_node.pos)
        # return the found path
        return path_to_sol



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

Maze = Maze(10,10)
Maze.kruskel()
Maze.draw_grid()
print(Maze.dfs(Maze.grid[0][0],Maze.grid[9][9]))
