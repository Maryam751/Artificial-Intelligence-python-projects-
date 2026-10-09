#implementation of BFS
class Graph():

    def __init__(self):
        self.graph={}

    def add_edge(self,node_a,node_b):

        if node_a not in self.graph:
            self.graph[node_a] = []
      
        if node_b not in self.graph:
            self.graph[node_b] = []

        self.graph[node_a].append(node_b)
        self.graph[node_b].append(node_a)

    def bfs(self,start):
        queue=[]
        visited=[]

        #starting node in queue
        queue.append(start)
        # start node as visited node
        visited.append(start)

        while len(queue)>0:
            #removing first node from queue 
            current=queue.pop(0)
            print(current,end=" ")

            #checking all neighbours
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    #putting neighbour in queue
                    queue.append(neighbour)
                    # mark neighbour as visited
                    visited.append(neighbour)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,4)
g.add_edge(1,3)
g.add_edge(4,3)
g.add_edge(1,2)
g.add_edge(3,2)


print("BFS TRAVERSAL:")
g.bfs(2)

    