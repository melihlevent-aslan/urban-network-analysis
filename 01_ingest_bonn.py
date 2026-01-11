import osmnx as ox
import time

# --- CONFIGURATION ---
CITY_QUERY = "Bonn, Germany"
NETWORK_TYPE = "walk"
OUTPUT_FILENAME = "bonn_walk_network.graphml"

def ingest_data():
    print(f"--- Starting Ingestion for {CITY_QUERY} ---")
    start_time = time.time()

    # 1. Download
    print(f"Downloading {NETWORK_TYPE} network... (this may take a moment)")
    G = ox.graph_from_place(CITY_QUERY, network_type=NETWORK_TYPE, simplify=True)

    # 2. Stats
    nodes = len(G.nodes)
    edges = len(G.edges)
    print(f"Download Complete. Graph Stats: {nodes} Nodes, {edges} Edges.")

    # 3. SAVE THE DATA FIRST 
    print(f"Saving graph to {OUTPUT_FILENAME}...")
    ox.save_graphml(G, filepath=OUTPUT_FILENAME)
    print("Graph successfully saved. Your data is safe.")

    # 4. Visualization 
    print("Generating static map (This might take 1-2 mins for large cities)...")
    try:
        fig, ax = ox.plot_graph(G, show=False, close=True, filepath="bonn_static_map.png", save=True, node_size=0)
        print("Static map saved as 'bonn_static_map.png'.")
    except Exception as e:
        print(f"Skipping visualization due to error: {e}")

    elapsed = time.time() - start_time
    print(f"--- Process finished in {elapsed:.2f} seconds ---")

if __name__ == "__main__":
    ingest_data()