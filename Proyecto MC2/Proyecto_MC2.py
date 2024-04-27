import networkx as nx
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Configuración inicial del grafo y la interfaz
network = nx.Graph()
window = tk.Tk()
window.title("Visualización de Grafos con Tkinter y NetworkX")
window.configure(bg='#8a8fa3')  # Nuevo color de fondo

# Ajuste del tamaño de la ventana
window.geometry('1200x700')  # Ampliado para acomodar dos gráficos

# Interfaz para añadir nodos
node_input = tk.Entry(window)
node_input.pack()
node_add_button = tk.Button(window, text="Añadir nodo", command=lambda: [network.add_node(node_input.get()), update_graph()], bg='#374254', fg='#ececec')
node_add_button.pack()

# Interfaz para añadir conexiones
connection_input1 = tk.Entry(window)
connection_input1.pack()
connection_input2 = tk.Entry(window)
connection_input2.pack()
edge_add_button = tk.Button(window, text="Añadir Arista", command=lambda: [network.add_edge(connection_input1.get(), connection_input2.get()), update_graph()], bg='#374254', fg='#ececec')
edge_add_button.pack()

# Botón para mostrar información del grafo
info_button = tk.Button(window, text="Mostrar información en consola", command=lambda: print("Total nodos:", network.number_of_nodes(), "\nTotal conexiones:", network.number_of_edges()), bg='#374254', fg='#ececec')
info_button.pack()

# Área para visualizar los grafos
graph_figure = Figure(figsize=(10, 5))
original_axis = graph_figure.add_subplot(121)  # Gráfico original en la izquierda
search_axis = graph_figure.add_subplot(122)  # Gráfico de búsqueda en la derecha
graph_canvas = FigureCanvasTkAgg(graph_figure, window)
graph_canvas.get_tk_widget().pack()



def update_graph(bfs_paths=None):
    # Actualizar ambos ejes
    original_axis.clear()
    search_axis.clear()

    # Configuraciones de fondo para ambos gráficos
    original_axis.set_facecolor('#0E1424')
    search_axis.set_facecolor('#0E1424')

    layout = nx.spring_layout(network)

    # Dibujar el grafo original en el eje izquierdo
    nx.draw(network, pos=layout, ax=original_axis, with_labels=True, node_color='#adbbc6', edge_color='#adbbc6')

    # Dibujar el grafo con búsqueda en el eje derecho
    nx.draw(network, pos=layout, ax=search_axis, with_labels=True, node_color='#adbbc6', edge_color='#adbbc6')
    if bfs_paths:
        nx.draw_networkx_edges(network, pos=layout, edgelist=bfs_paths, edge_color='#374254', ax=search_axis)
        nx.draw_networkx_nodes(network, pos=layout, nodelist=[node_input.get()] + [v for u, v in bfs_paths], node_color='#374254', ax=search_axis)

    graph_canvas.draw()


def ancho():
    bfs_paths = list(nx.bfs_edges(network, source=node_input.get()))
    update_graph(bfs_paths)

ancho_button = tk.Button(window, text="Búsqueda a lo ancho", command=ancho, bg='#374254', fg='#ececec')
ancho_button.pack()


def execute_dfs():
    dfs_paths = list(nx.dfs_edges(network, source=node_input.get()))
    update_graph(dfs_paths)

dfs_button = tk.Button(window, text="Búsqueda en profundidad", command=execute_dfs, bg='#374254', fg='#ececec')
dfs_button.pack()

window.mainloop()
