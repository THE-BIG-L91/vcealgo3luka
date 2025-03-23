import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.neighbours = []

    def __str__(self):
        return str(self.id)
        
    def add_neighbour(self, neighbour):
      if neighbour not in self.neighbours:
        self.neighbours.append(neighbour)
        self.sort_neighbours()
        
        
    def sort_neighbours(self):
      sorted = []
      while len(self.neighbours) > 0:
        smallest = self.neighbours[0]
        for node in self.neighbours:
          if node.id < smallest.id:
            smallest = node
        sorted.append(smallest)
        self.neighbours.remove(smallest)
      self.neighbours = sorted

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        self.id1 = source.id
        self.id2 = target.id
        self.color = 'black'

class RandomGraph:

  def __init__(self,V_N,E_N):
    # Creates a random graph objects with V_N vertices each with E_N edges
    self.edges = []
    self.nodes = [Node(i) for i in range(1,V_N+1)]
    
    for node in self.nodes:
    
      neighbours = random.sample(self.nodes,3)
      for neighbour in neighbours:
        if node != neighbour and self.get_weight(node.id, neighbour.id) == -1:
          rw = random.randint(1,7)
          edge = Edge(node, neighbour, rw)
          self.edges.append(edge)
          node.add_neighbour(neighbour)
          neighbour.add_neighbour(node)

  def get_weight(self, node1, node2):
    # Returns the edge weight between two nodes
    for edge in self.edges:
      if edge.id1 == node1 and edge.id2 == node2:
        return edge.weight
      if edge.id2 == node1 and edge.id1 == node2:
        return edge.weight
    return -1

  def set_colour(self, id1, id2, colour):
    # Sets the edge between id1 and id2 to the stated colour
    for edge in self.edges:
      if edge.id1 == id1 and edge.id2 == id2:
        edge.color = colour
      if edge.id1 == id2 and edge.id2 == id1:
        edge.color = colour  

  def display_graph(self):
    
    self.G = nx.Graph()
    for node in self.nodes:
      self.G.add_node(node)
    for edge in self.edges:
      self.G.add_edge(edge.source, edge.target, weight = edge.weight)
    pos = nx.spring_layout(self.G, seed=42)
    nx.draw(self.G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
      
    #edge_labels = nx.get_edge_attributes(self.G, 'weight')
    edge_labels = {}
    edge_colors = []
    for edge in self.edges:
      edge_colors.append(edge.color)  
      edge_labels[(edge.source, edge.target)]= edge.weight
    
    
    
    nx.draw(self.G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold', edge_color=edge_colors, width=2.0)
    nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

    plt.title("Prims")
    plt.axis('off')
    plt.show()

  def list_nodes_and_edges(self):
    for node in self.nodes:
      print(f"Node: {node.id}")
    for edge in self.edges:
      print(f"Edge from {edge.id1} to {edge.id2} with weight {edge.weight} and colour {edge.color}")


  def reset_visits(self):
    for node in self.nodes:
      node.visited = False

  def Prims(self):
    # prims
    final = []
    list_of_nodes = []
    list_of_nodes.append(self.nodes[0])
    self.nodes[0].visited = True

    
    while (len(list_of_nodes) <= len(self.nodes)): 
      lowest_weight = 2**32
      lowest_found_node = 0
      final_node = 0

      for node1 in list_of_nodes:
        for found in node1.neighbours:
          if found.visited == True or found in list_of_nodes:
            continue

          weight = self.get_weight(found.id,node1.id)
          if weight < lowest_weight:
            lowest_found_node = found
            lowest_weight = weight
            final_node = node1

      if lowest_found_node == 0:
        break
      list_of_nodes.append(lowest_found_node)
      final.append([final_node, lowest_found_node, lowest_weight])
      # I don't know what's going on with the set_colour function, but I just can't get it to work.
      print(f"connection: {final_node.id}, {lowest_found_node.id} ")
      lowest_found_node.visited = True

    print(f"Total list of nodes: {len(list_of_nodes)}")
    print(f"Total list of edges: {len(final)}")
    for i in (final):
       print(f"Edge: {i[0].id} and {i[1].id} with a weight of {i[2]}")
    
    # Pick a vertex
    # Select the cheapest edge that doesn't connect to something already in the list
    # Set color to 'red'
    # Repeat until number of edges = n-1


RG = RandomGraph(10,3)
RG.Prims()
#RG.list_nodes_and_edges()
RG.display_graph()
