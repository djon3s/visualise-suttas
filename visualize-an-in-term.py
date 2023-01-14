import json
from urllib.request import urlopen
from anytree import Node, RenderTree
from graphviz import Digraph

url = "https://raw.githubusercontent.com/suttacentral/sc-data/master/structure/tree/sutta/an-tree.json"
response = urlopen(url)
json_data = json.loads(response.read())

def build_tree(d, parent=None):
    for k, v in d.items():
        if isinstance(v, dict):
            node = Node(k, parent=parent)
            build_tree(v, parent=node)
        elif isinstance(v, list):
            node = Node(k, parent=parent)
            for item in v:
                if isinstance(item, dict):
                    build_tree(item, parent=node)
                else:
                    Node(item, parent=node)
        else:
            Node(k, parent=parent, value=v)

root = Node("root")
build_tree(json_data, parent=root)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

