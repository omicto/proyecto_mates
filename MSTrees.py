from tkinter import *
# from node import Node
from graph import Graph

class Main():


    def __init__(self):
        # Iniciamos con un canvas vacio
        self.canvas = None
        # Necesario iniciar en falso para cuestiones de anadir aristas :)
        self.a_dot_is_already_clicked = False
        # Nuestro grafo vacio
        self.graph = Graph()
        # Es mas o menos redudante, pero para numerar los ids hacemos algo parecido a Graph().num_vertices
        self.current_id = 0

    def on_canvas_click(self, event):
        self.new_dot(event.x, event.y)

    def new_dot(self, x, y):
        dot = self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", tags="dot")
        # Usamos las coordenadas de pantalla como id para nuestro nodo. Las tuplas funcionan ya que
        # son un tipo de dato inmutable :)

        print(self.canvas.coords(dot))
        # self.starting_point = self.graph.add_vertex(crds, dot)
        self.starting_point = self.graph.add_vertex(self.current_id)
        self.starting_point.set_pos(x,y)
        #Aumentamos la cuenta actual de vertices en uno
        self.current_id += 1

        print("Nodo ({}) creado en {}".format(self.current_id, (x,y)))

        # Incrementamos la id
        # self.current_id += 1

    def on_dot_click(self, event):
        if self.a_dot_is_already_clicked: # Si ya hicimos click en otro vertice
            # Identificamos el punto en el que hicimos click
            w = self.identify_dot(event)
            w_id = w.get_id()
            # Recuperamos el vertice correspondiente
            # w = self.graph.get_vertex(id)
            # Renombramos la id del vertice que ya traiamos, por conveniencia
            v = self.almacenar_vertice
            v_id = v.get_id()


            # Reseteamos condiciones anteriores
            self.a_dot_is_already_clicked = False
            self.canvas.itemconfig(self.selected_dot, fill="black")

            if v_id == w_id:
                print("No se pueden añadir lazos")
                return

            (x_0, y_0) = v.get_pos()
            (x_1, y_1) = w.get_pos()

            # Amablemente pedimos el peso de la arista a añadir
            weight = float(input("Dale un peso (no negativo, porfa) a la arista: "))

            self.graph.add_edge(v_id, w_id, weight)
            self.canvas.create_line(x_0, y_0, x_1, y_1, tags = "edge")
            print("Añadida arista que va de ({}, {})".format(v_id, w_id))
            # print(self.graph.get_vertex(v_id))

        else:
            # Identificamos el punto en el que hicimos click
            v  = self.identify_dot(event)
            # Recuperamos el vertice correspondiente
            # v = self.graph.get_vertex(id)
            # Almacenamos el id del vertice encontrado
            self.almacenar_vertice = v


            self.a_dot_is_already_clicked = True
            # Tenemos que visualizar ese hecho. Lo almacenamos temporalmente para poder regresarlo a su estado original
            self.selected_dot = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfig(self.selected_dot, fill = "cyan")

            print("Seleccionado vertice. Esperando accion")

    def identify_dot(self, event):
        '''
        Regresa un nodo segun las coordenadas
        '''
        # Identificamos el punto sobre el que hicimos click
        dot = self.canvas.find_closest(event.x, event.y)
        # Obtenemos su posicion
        pos = self.canvas.coords(dot)
        # Encontramos su id en base a la posicion
        coord_id = (int(pos[0] + 4), int(pos[1] + 4))
        x,y = coord_id

        return self.graph.get_node_with_pos(x, y)

    def draw_mst(self, event):
        self.graph.prim(self.starting_point)

        # Iteramos atraves del grafo
        for v in self.graph:
            w = v.get_pred()
            if w is not None:
                # Si v y w están conectados
                print("Marcada arista ({}, {}), peso {}".format(v.get_id(), w.get_id(), v.get_weight(w) ))
                x0, y0 = v.get_pos()
                x1, y1 = w.get_pos()

                self.canvas.create_line(x0, y0, x1, y1, tags="MSTedge", fill= "red", width = 2)

    def main(self):
        root = Tk()

        self.canvas = Canvas(root, width=350, height=350)
        # Le indicamos al canvas las acciones por las que debe estar al pendiente
        self.canvas.bind("<Double-1>", self.on_canvas_click)    # Doble click izq
        self.canvas.bind("<Control-Button-1>", self.draw_mst)   # Ctrl + Click Izq en el canvas
        self.canvas.tag_bind("dot", "<Button-1>", self.on_dot_click) # Click izq sobre dot
        self.canvas.pack()

        root.mainloop()

        # Que nos imprima el grafo a ver que tal

        self.test()

    def test(self):

        g = self.graph

        g.prim(self.starting_point)
        for v in g:
            print('g.vert_dict[{}]={}'.format(v.get_id(), g.vert_dict[v.get_id()]))
            print("predecesor = {}".format(v.get_pred()))

if __name__ == "__main__":
    Main().main()