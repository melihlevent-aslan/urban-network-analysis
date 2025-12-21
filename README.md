# Graph-Based Urban Network Analysis

![Python](https://img.shields.io/badge/Language-Python-blue)
![Graph Theory](https://img.shields.io/badge/Topic-Network_Analysis-green)

## Project Overview
This project focuses on the algorithmic analysis of urban street networks to quantify accessibility and walkability. By modeling the city as a graph structure, it computes spatial metrics such as shortest-path distances to critical infrastructure and centrality measures for every land parcel.

## Theoretical Background
The project applies concepts from Graph Theory and Spatial Decision Support Systems (SDSS). It aims to provide decision-makers with quantitative data regarding service gaps in public transportation and urban facility distribution.

## Key Features
* **Graph Construction:** Automated retrieval of street networks from OpenStreetMap (OSM) via OSMnx.
* **Walkability Index:** Calculation of isochrones and impedance-based accessibility scores for residential areas.
* **Network Centrality:** Computation of Betweenness and Closeness centrality to identify critical junctions.

## Tech Stack
* **Network Analysis:** NetworkX, OSMnx
* **Data Handling:** Pandas, GeoPandas
* **Visualization:** Matplotlib, Folium (Interactive Web Maps)

## Roadmap
* [ ] Ingest Bonn street network data.
* [ ] Implement Dijkstra's algorithm for single-source shortest path problems.
* [ ] Visualize accessibility heatmaps for public transit stops.

---
Melih Levent Aslan | M.Sc. Student, University of Bonn
