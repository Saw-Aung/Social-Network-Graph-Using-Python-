import networkx as nx
import matplotlib.pyplot as plt

lists = []

min=5

max=25

for i in range(min, max):
   print(10*i)
   ws03 = nx.watts_strogatz_graph(10*i, 4, 0.3)
   lists.append(nx.average_shortest_path_length(ws03))

   nx.draw_circular(ws03, node_size=10, node_color='red')
   print("L =", nx.average_shortest_path_length(ws03))

print(lists)

import numpy as np

list_a=[]
for x in range(min , max):
   list_a.append(np.log(10*x))

print(list_a)

import pandas as pd
df = pd.DataFrame(
    list_a
)
df[1] =lists

df.columns = ['totalnumberofsites','meangraphdistance']

df

import numpy
import pandas
import matplotlib.pyplot as plt
df.plot()
df.plot.scatter(x='totalnumberofsites', y='meangraphdistance')