"""
Author: Ramiz Raja
Created on: 27/01/2020
"""
import networkx as nx
import pickle
from plotly.graph_objs import *
import random

class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
		print(G)
	return Map(G)