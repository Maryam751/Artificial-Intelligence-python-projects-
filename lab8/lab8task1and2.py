#task 1
class Graph:
    def __init__(self):
        self.graph = {}
        self.heuristic = {}

    # Function to add edges
    def add_edge(self, city1, city2, distance):
        if city1 not in self.graph:
            self.graph[city1] = []

        if city2 not in self.graph:
            self.graph[city2] = []

        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))

    # Greedy Best First Search
    def Greedy(self, start, goal):
        open_list = [start]
        visited = []
        path = {start: [start]}

        while open_list:
            current = min(open_list, key=lambda x: self.heuristic[x])
            open_list.remove(current)

            print("Current City:", current)

            if current == goal:
                print("Goal Reached!")
                print("Final Path:", " -> ".join(path[current]))
                return

            visited.append(current)

            for neighbor, distance in self.graph[current]:
                if neighbor not in visited and neighbor not in open_list:
                    open_list.append(neighbor)
                    path[neighbor] = path[current] + [neighbor]

        print("Goal not reached!")

#task2
    # A Star Search
    def AStar(self, start, goal):
        open_list = [start]
        visited = []

        g_cost = {start: 0}
        path = {start: [start]}

        while open_list:
            current = min(
                open_list,
                key=lambda x: g_cost[x] + self.heuristic[x]
            )

            open_list.remove(current)

            print("Current City:", current)

            if current == goal:
                print("Goal Reached!")
                print("Final Path:", " -> ".join(path[current]))
                print("Path Cost:", g_cost[current])
                return

            visited.append(current)

            for neighbor, distance in self.graph[current]:

                total_cost = g_cost[current] + distance

                if neighbor in visited:
                    continue

                if neighbor not in g_cost or total_cost < g_cost[neighbor]:

                    g_cost[neighbor] = total_cost
                    path[neighbor] = path[current] + [neighbor]

                    if neighbor not in open_list:
                        open_list.append(neighbor)

        print("Goal not reached!")


# Create Graph
g = Graph()

# Add city connections
g.add_edge("Arad", "Zerind", 75)
g.add_edge("Arad", "Sibiu", 140)
g.add_edge("Arad", "Timisoara", 118)
g.add_edge("Zerind", "Oradea", 71)
g.add_edge("Oradea", "Sibiu", 151)
g.add_edge("Sibiu", "Fagaras", 99)
g.add_edge("Sibiu", "Rimnicu Vilcea", 80)
g.add_edge("Timisoara", "Lugoj", 111)
g.add_edge("Lugoj", "Mehadia", 70)
g.add_edge("Mehadia", "Drobeta", 75)
g.add_edge("Drobeta", "Craiova", 120)
g.add_edge("Craiova", "Rimnicu Vilcea", 146)
g.add_edge("Craiova", "Pitesti", 138)
g.add_edge("Rimnicu Vilcea", "Pitesti", 97)
g.add_edge("Fagaras", "Bucharest", 211)
g.add_edge("Pitesti", "Bucharest", 101)
g.add_edge("Bucharest", "Giurgiu", 90)
g.add_edge("Bucharest", "Urziceni", 85)
g.add_edge("Urziceni", "Hirsova", 98)
g.add_edge("Hirsova", "Eforie", 86)
g.add_edge("Urziceni", "Vaslui", 142)
g.add_edge("Vaslui", "Iasi", 92)
g.add_edge("Iasi", "Neamt", 87)


# Heuristic Dictionary
g.heuristic = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


print("----- GREEDY BEST FIRST SEARCH -----")
g.Greedy("Arad", "Bucharest")

print("\n----- A STAR SEARCH -----")
g.AStar("Arad", "Bucharest")



