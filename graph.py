from node import Node
from priorityqueue import PriorityQueue
import sys

class Graph:


    def __init__(self):
        '''
        Iniciamos con un diccionario de vertices vacio. El diccionario es de la forma
        vert_dict = {"id": Nodo} donde id es de hecho nodo.id
        '''
        self.vert_dict = {}
        self.num_vertices = 0


    def __iter__(self):
        # Regresamos un iterable con todos los nodos del grafo
        return iter(self.vert_dict.values())

    def add_vertex(self, key, oval):
        # Actualizamos el numero de vertices
        self.num_vertices += 1
        new_vertex = Node(key, oval)
        # Añadimos el nuevo vertice al diccionario
        self.vert_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        # Buscamos un vertice dada su id y regresamos el Node correspondiente
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        '''
         Revisamos que los vertices de inicio(frm) y fin(to) de la arista
         esten en el diccionario.
         El costo default es cero.
        '''

        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        # Asignamos cada vertice como vecino del otro
        # recordemos que la arista (v,w) = (w,v)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        # Lista con todas las id de los vertices
        return self.vert_dict.keys()

    def prim(self, start):
        # Ejecutamos el algoritmo in-place
        pq = PriorityQueue()
        for v in self:
            v.set_distance(sys.maxsize)
            v.set_pred(None)

        start.set_distance(0)
        pq.buildHeap([(v.get_distance(), v) for v in self])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.get_connections():
                newCost = currentVert.get_weight(nextVert)
                if nextVert in pq and newCost < nextVert.get_distance():
                    nextVert.set_pred(currentVert)
                    nextVert.set_distance(newCost)
                    pq.decreaseKey(nextVert, newCost)




if __name__ == '__main__':
    # Pruebas. No funcionan debido a la integracion con la interfaz :)
    '''
    g = Graph()
    
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 3)


    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( {} , {}, {})'.format( vid, wid, v.get_weight(w)))

    for v in g:
        print ('g.vert_dict[{}]={}'.format(v.get_id(), g.vert_dict[v.get_id()]))'''
