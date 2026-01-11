# Graph-Based Urban Network Analysis: Bonn Digital Twin

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![OSMnx](https://img.shields.io/badge/OSMnx-v2.0-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

> **A Spatial Decision Support System (SDSS) for the "15-Minute City"**
> *Developed as part of the M.Sc. Geodetic Engineering Program, University of Bonn.*

---

##  Overview
This project automates the quantitative analysis of urban street networks. By ingesting raw OpenStreetMap (OSM) data, it constructs a mathematical graph of Bonn, Germany, to calculate **accessibility**, **centrality**, and **optimal routing**.

The system serves as a "Digital Twin" component for surveyors (*ÖbVI*) and urban planners, moving beyond static maps to dynamic, algorithmic assessment of city infrastructure.

---

##  Key Results (The "Tech Edge")

### 1. The Nervous System (Betweenness Centrality)
*Analysis of 39,000+ nodes to identify critical infrastructure bottlenecks.*
![Centrality Heatmap](bonn_centrality.png)
> **Insight:** Yellow nodes represent intersections with the highest mathematical flow potential. These are the prime locations for commercial development or advertising.

### 2. The 15-Minute City (Isochrone Analysis)
*Quantifying walkability from the University Main Building (Hofgarten).*
![Walkability Zones](bonn_walkability.png)
> **Legend:**
> * 🔴 **Red:** < 5 Minutes (Campus Core)
> * 🟡 **Yellow:** < 10 Minutes (Market/Rhine)
> * 🟢 **Green:** < 15 Minutes (District Court)

### 3. The Surveyor's Commute (Shortest Path)
*Optimizing the workflow between University and Land Registry (Amtsgericht).*
![Surveyor Route](bonn_route.png)
> **Result:** The algorithm determined the optimal path length to be **621.85 meters**, correcting for geodetic coordinate shifts.

---

##  Tech Stack
* **Core Engine:** `OSMnx 2.0`, `NetworkX`
* **Geospatial Processing:** `GeoPandas`, `Shapely`
* **Visualization:** `Folium` (Interactive Web Maps), `Matplotlib` (Static Rendering)
* **Algorithm:** Dijkstra’s Shortest Path, Brandes' Betweenness Centrality

---

##  Project Structure
```bash
├── 01_ingest_bonn.py          # Downloads raw vector data from OSM
├── 02_centrality.py           # Calculates Betweenness Centrality
├── 03_visualize.py            # Generates static heatmaps
├── 04_interactive_map.py      # Creates interactive HTML dashboard
├── 05_walkability.py          # Generates 15-min Isochrones
├── 06_shortest_path.py        # Runs Dijkstra Routing (Surveyor Commute)
├── 07_master_dashboard.py     # COMBINES EVERYTHING into one Web-GIS
├── bonn_master_dashboard.html # <--- The Final Output File
└── README.md
```
---
*Melih Levent Aslan | M.Sc. Geodetic Engineering Student, University of Bonn*