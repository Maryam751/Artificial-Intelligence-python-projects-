class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    # Iterative DFS
    def dfs_stack(self, start, goal):
        stack = [start]
        visited = []

        print(f"DFS Traversal (Stack) starting from node '{start}'")

        while stack:
            v = stack.pop()

            if v not in visited:
                visited.append(v)
                print(f"Visited: {v}")

               
                if  v == goal:
                    print(f"Goal node '{goal}' reached!")
                    break
               

                # Push neighbors in reverse order
                for neighbor in reversed(self.adj.get(v, [])):
                    if neighbor not in visited:
                        stack.append(neighbor) 

        else:
            print("Goal NOt reeched ")            



g = Graph()

# Add edges
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

g.dfs_stack(start='A', goal='G')




