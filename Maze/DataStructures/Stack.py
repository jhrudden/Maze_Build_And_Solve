class Stack:
    def __init__(self):
        self.data = [];

    def add(self, item):
        self.data.insert(0,item);

    def remove(self):
        return self.data.pop(0);
