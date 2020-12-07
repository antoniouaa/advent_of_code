import networkx as nx
import re

source_regex = r"^(\w+ \w+)"
dest_regex = r"(\d+) (\w+ \w+)"

with open("input.txt") as f:
    lines = [line.strip() for line in f]

graph = nx.DiGraph()
for line in lines:
    source = re.findall(source_regex, line)
    dest = re.findall(dest_regex, line)
    for d in dest:
        graph.add_edge(source[0], d[1], weight=int(d[0]))

num = 0
for node in graph.nodes:
    try:
        if nx.shortest_path_length(graph,
                                   source=node, target="shiny gold"):
            num += 1
    except:
        continue

print(num)

bags = -1
top_level = [(1, "shiny gold")]
while top_level:
    weight, color = top_level.pop()
    bags += weight
    top_level.extend((weight * graph.edges[src, dest]["weight"], dest)
                     for src, dest in nx.dfs_edges(graph, source=color, depth_limit=1))
    print(top_level)

print(bags)
