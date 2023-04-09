import csv
import networkx as nx
import matplotlib.pyplot as plt

def generate_family_tree(csv_file):
    # Create an empty graph
    G = nx.Graph()
    
    # Read the CSV file and add nodes and edges to the graph
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip header
        for row in reader:
            member1, member2, relation = row
            G.add_node(member1)
            G.add_node(member2)
            G.add_edge(member1, member2, relation=relation)
    
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

# Example usage
generate_family_tree('family_tree.csv')
