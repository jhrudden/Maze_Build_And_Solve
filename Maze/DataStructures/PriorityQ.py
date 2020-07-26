
class PriorityQ:
    def __init__(self):
        self.queue = []

    # insert an element into its designated place in an array
    def insert(self, item):
        # insert the element into end of heap
        self.queue.append(item);
        # upheap the item untill it is its designated place
        self.up_heap(len(self.queue) - 1);

    # remove the top item of a heap
    def remove_min(self):
        # swap first an last items of heap
        last_index = len(self.queue) - 1
        temp = self.queue[0]
        self.queue[0] = self.queue[last_index]
        self.queue[last_index] = temp
        # downheap so that new top of heap gets put in its designated place
        min = self.queue.pop(last_index)
        self.down_heap(0);

        return min;

    # Recursively move a given element up in a heap if it is smaller than its
    # parent
    def up_heap(self, index):
        parent = (index - 1) // 2

        # if weight of current value is smaller than the parent, then swap them
        if self.queue[index].compare(self.queue[parent]) < 0 and index > 0:
            temp = self.queue[parent];
            self.queue[parent] = self.queue[index];
            self.queue[index] = temp;
            index = parent

            # recursively continue the upheap untill item is settled
            self.up_heap(index)

    # Move an element at a given index down a heap to its designated spot, while
    # also keeping heap properties. (heap tree is balanced and no parent is
    # larger than children)
    def down_heap(self, index):
        # base case
        if index >= len(self.queue) - 1:
            return;
        l_child_i = index*2 + 1;
        r_child_i = index*2 + 2;

        # want to swap current value with smallest of its children nodes, in
        # order to maintain heap property (no parent larger than children)
        if l_child_i <= len(self.queue) - 1:
            min_child_i = l_child_i
            if r_child_i <= len(self.queue) - 1:
                if self.queue[l_child_i].compare(self.queue[r_child_i])>0:
                    min_child_i = r_child_i
        else:
            return;

        # if parent is larger than smallest child, swap them
        if self.queue[index].compare(self.queue[min_child_i]) > 0:
            temp = self.queue[min_child_i]
            self.queue[min_child_i] = self.queue[index]
            self.queue[index] = temp
            index = min_child_i

            # recursively downheap, until element is in its correct place
            self.down_heap(index)

    # is this priority queue empty?
    def is_empty(self):
        return len(self.queue) == 0;
