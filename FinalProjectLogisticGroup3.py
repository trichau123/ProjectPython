###Group 3 Project Logistic
# DataStructure
#
#Tri Chau
#Jesus Hilario
#Joshua Sarria
#Lucas Vieira

from collections import defaultdict
from heapq import *
import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

a = []
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        a.append((frm,to,cost))

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

# t  is node begin and f is finish node
def dijkstra(edges, f, t):
    # g is a dictionary key, values
    # list is type of g dictionary
    g = defaultdict(list)

    #edges l node begin ,r node finish and c path (weighted)
    for l, r, c in edges:
        # add values ("c", r) add  the key "l" of g["l"]
        g[l].append((c, r))
    # seen set() will convert list, tuple to order list {1,2,3}
    # q [(cost: 0, fishnish node: f, path [])]
    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        # heapq represent a priority queue. whenever the elements are pushed or popped
        # heap structure maintain and pop the smallest of heap element min heap
        # cost: . v1 last node  . path is distance
        (cost, v1, path) = heappop(q)
        # if dont see last node in seen
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1 == t:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))


    return (float("inf"), [])


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('H')
    g.add_vertex('I')
    g.add_vertex('J')
    g.add_vertex('K')
    g.add_vertex('L')
    g.add_vertex('M')
    g.add_vertex('N')

    g.add_edge('A','B',2)
    g.add_edge('B','D',2)
    g.add_edge('C','A',4)
    g.add_edge('C','F',2)
    g.add_edge('C','E',2)
    g.add_edge('D','B',2)
    g.add_edge('D','G',3)
    g.add_edge('D','H',6)
    g.add_edge('E','C',2)
    g.add_edge('E','K',4)
    g.add_edge('F','G',6)
    g.add_edge('F','C',2)
    g.add_edge('F','E',4)
    g.add_edge('F','J',2)
    g.add_edge('G','I',3)
    g.add_edge('G','F',6)
    g.add_edge('H','I',2)
    g.add_edge('H','D',6)
    g.add_edge('I','G',3)
    g.add_edge('I','J',6)
    g.add_edge('J','I',6)
    g.add_edge('J','L',5)
    g.add_edge('J','M',3)
    g.add_edge('K','M',3)
    g.add_edge('L','H',3)
    g.add_edge('L','N',4)
    g.add_edge('L','J',5)
    g.add_edge('M','J',3)
    g.add_edge('M','K',3)
    g.add_edge('N','L',4)
    g.add_edge('N','M',2)

    print ('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    print ("The shortest path from A to  N and go back is: ")
    print ("A -> N:")
    print (dijkstra(a, "A", "N"))
    print ("N -> A:")
    print (dijkstra(a, "N", "A"))

