class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    # Depth Limited Search
    def DLS(self, node, goal, limit):

        print(node, end=" ")

        if node == goal:
            return True

        if limit <= 0:
            return False

        for neighbor in self.graph[node]:

            if self.DLS(neighbor, goal, limit - 1):
                return True

        return False

    # Iterative Deepening Search
    def IDS(self, start, goal, max_depth):

        for limit in range(max_depth + 1):

            print("\nDepth Limit:", limit)
            print("Traversal:", end=" ")

            if self.DLS(start, goal, limit):
                print("\nGoal Found!")
                return True

        print("\nGoal Not Found!")
        return False


# create Graph
g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('D', 'G')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')


# apply IDS
g.IDS('A', 'G', 5)


