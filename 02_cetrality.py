import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# --- CONFIG ---
INPUT_FILENAME = "bonn_walk_network.graphml"
OUTPUT_FILENAME = "bonn_centrality.graphml" 
# Coordinates for Uni Bonn (Hofgarten)
CENTER_POINT = (50.733, 7.102) 
DIST_METERS = 1000  

def analyze_centrality():
    print("1. Loading graph from disk...")
    G = ox.load_graphml(INPUT_FILENAME)
    G_proj = ox.project_graph(G)
    
    print(f"2. Extracting subgraph ({DIST_METERS}m around University)...")
    G_sub = ox.graph_from_point(CENTER_POINT, dist=DIST_METERS, network_type='walk', simplify=True)
    print(f"   Subgraph Stats: {len(G_sub.nodes)} nodes.")

    print("3. Computing Betweenness Centrality (Math)...")
    bc = nx.betweenness_centrality(nx.MultiDiGraph(G_sub), weight='length')
    nx.set_node_attributes(G_sub, bc, 'betweenness')
    
    print(f"   >>> Saving analysis results to {OUTPUT_FILENAME}...")
    ox.save_graphml(G_sub, filepath=OUTPUT_FILENAME)
    print("   >>> Data saved! Your analysis is now safe on disk.")

    print("4. Attempting to Plot Heatmap...")
    try:
        nc = ox.plot.get_node_colors_by_attr(G_sub, 'betweenness', cmap='inferno')
        
        # Plot
        fig, ax = ox.plot_graph(G_sub, node_color=nc, node_size=30, edge_linewidth=0.5, 
                                bgcolor='k', show=False, close=True, filepath="bonn_centrality.png", save=True)
        print("Analysis Complete! Open 'bonn_centrality.png' to see the heatmap.")
        
    except Exception as e:
        print(f"(!) Plotting failed, BUT your data is safe in '{OUTPUT_FILENAME}'.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    analyze_centrality()