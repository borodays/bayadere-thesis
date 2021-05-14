import csv
import os
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community
import bokeh
from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool, MultiLine, Plot, Range1d, ResetTool, GraphRenderer)
from bokeh.palettes import Set3_8
from bokeh.plotting import from_networkx
from bokeh.embed import components

print(os.getcwd())
os.chdir("/Users/sofiyaboroday/Documents/GitHub/thesis.io/Thesis Visualizations/")
with open('firstNodes.csv', 'r') as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    # Retrieve the data (using Python list comprhension and list slicing to remove the header row, see footnote 3)
    nodes = [n for n in nodereader][1:]

node_ids = [n[0] for n in nodes] # Get a list of only the node names

with open('firstEdges.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

print(len(node_ids))
print(len(edges))
print(edges)

G = nx.Graph()
G.add_nodes_from(node_ids)
G.add_edges_from(edges)

print(nx.info(G))

node_names = {}
node_types = {}
node_dates = {}
for node in nodes:
    node_names[node[0]] = node[1]
    node_types[node[0]] = node[2]
    node_dates[node[0]] = node[3]

print(node_names)

nx.set_node_attributes(G, node_names, 'Name')
nx.set_node_attributes(G, node_types, 'Type')
nx.set_node_attributes(G, node_dates, 'Date')

ballet_color = Set3_8[0]
choreographer_color = Set3_8[1]
dancer_color = Set3_8[2]
librettist_color = Set3_8[3]
travel_writer_color = Set3_8[4]
book_color = Set3_8[5]

node_colors = {}
edge_colors = {}

for node in nodes:
    if node[2] == "ballet":
        node_colors[node[0]] = ballet_color
    if node[2] == "choreographer":
        node_colors[node[0]] = choreographer_color
    if node[2] == "dancer":
        node_colors[node[0]] = dancer_color
    if node[2] == "librettist":
        node_colors[node[0]] = librettist_color
    if node[2] == "travel writer":
        node_colors[node[0]] = travel_writer_color
    if node[2] == "book":
        node_colors[node[0]] = book_color

nx.set_node_attributes(G, node_colors, "node_color")

plot = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "La Bayadère in Context"

node_hover_tool = HoverTool(tooltips=[("name", "@Name"), ("type", "@Type"), ("date", "@Date")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())
graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))


graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="node_color")
graph_renderer.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=0.8, line_width=1)
plot.renderers.append(graph_renderer)


script, div = components(plot)
output_file("interactive_graphs.html")

print(script)
print(div)
#show(plot)

print(bokeh.__version__)

print(os.getcwd())
with open('secondNodes.csv', 'r') as secondnodecsv: # Open the file
    secondnodereader = csv.reader(secondnodecsv) # Read the csv
    # Retrieve the data (using Python list comprhension and list slicing to remove the header row, see footnote 3)
    secondnodes = [n for n in secondnodereader][1:]

second_node_ids = [n[0] for n in secondnodes] # Get a list of only the node names

with open('secondEdges.csv', 'r') as secondedgecsv: # Open the file
    secondedgereader = csv.reader(secondedgecsv) # Read the csv
    secondedges = [tuple(e) for e in secondedgereader][1:] # Retrieve the data

print(len(second_node_ids))
print(len(secondedges))
print(secondedges)

G2 = nx.Graph()
G2.add_nodes_from(second_node_ids)
G2.add_edges_from(secondedges)

print(nx.info(G2))

second_node_names = {}
second_node_types = {}
for node in secondnodes:
    second_node_names[node[0]] = node[1]
    second_node_types[node[0]] = node[2]

print(second_node_names)

nx.set_node_attributes(G2, second_node_names, 'Name')
nx.set_node_attributes(G2, second_node_types, 'Type')

dance_color = Set3_8[0]
choreographer_color = Set3_8[1]
dancer_color = Set3_8[2]
scholar_color = Set3_8[3]
company_color = Set3_8[4]
publication_color = Set3_8[5]
internet_color = Set3_8[6]

node_colors_2 = {}
edge_colors_2 = {}

for node in secondnodes:
    if node[2] == "dance":
        node_colors_2[node[0]] = dance_color
    if node[2] == "choreographer":
        node_colors_2[node[0]] = choreographer_color
    if node[2] == "dancer":
        node_colors_2[node[0]] = dancer_color
    if node[2] == "scholar":
        node_colors_2[node[0]] = scholar_color
    if node[2] == "company":
        node_colors_2[node[0]] = company_color
    if node[2] == "publication":
        node_colors_2[node[0]] = publication_color
    if node[2] == "Internet":
        node_colors_2[node[0]] = internet_color

nx.set_node_attributes(G2, node_colors_2, "node_color")

plot2 = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot2.title.text = "La Bayadère in Context: 2021"

node_hover_tool_2 = HoverTool(tooltips=[("name", "@Name"), ("type", "@Type")])
plot2.add_tools(node_hover_tool_2, BoxZoomTool(), ResetTool())
graph_renderer_2 = from_networkx(G2, nx.spring_layout, scale=1, center=(0, 0))


graph_renderer_2.node_renderer.glyph = Circle(size=15, fill_color="node_color")
graph_renderer_2.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=0.8, line_width=1)
plot2.renderers.append(graph_renderer_2)


script2, div2 = components(plot2)
output_file("interactive_graphs_2.html")

print(script2)
print(div2)
#show(plot)

print(bokeh.__version__)