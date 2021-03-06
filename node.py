from tkinter import *
class Node:
    def __init__(self, key):
        '''
        Iniciamos con una id para el vertice.
        Oval es el circulo que representa al vertice
        '''
        self.id = key
        # self.oval = oval
        self.pred = None
        # Diccionario de vertices adyacentes
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adyacente(s): ' + str([v.id for v in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        '''
        Añadimos un vertice adyacente al diccionario. La clave es el nodo vecino
        y el valor es el peso.
        Peso por defecto: cero.
        '''
        self.adjacent[neighbor] = weight

    def get_connections(self):
        # Regresamos una lista con todos los vertices adyacentes al vertice actual
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        # Regresamos el peso de la arista (self - neighbor)
        return self.adjacent[neighbor]

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_pos(self, x, y):
        # Coordenadas
        self.x = x
        self.y = y

    def get_distance(self):
        return self.dist

    def get_pred(self):
        return self.pred

    def get_pos(self):
        return (self.x, self.y)