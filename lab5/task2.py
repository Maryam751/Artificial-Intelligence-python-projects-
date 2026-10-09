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

    def bfs(self,start,goal):
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

            if current == goal :
                print("Goal Found! ")
                return

            #checking all neighbours
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    #putting neighbour in queue
                    queue.append(neighbour)
                    # mark neighbour as visited
                    visited.append(neighbour)

        print("\n Goal not found")            

g = Graph()
g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('B','K')
g.add_edge('B','J')
g.add_edge('D','G')
g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')
g.add_edge('K','N')
g.add_edge('K','M')
g.add_edge('I','L')

print("BFS TRAVERSAL:")
g.bfs('A','G')

    