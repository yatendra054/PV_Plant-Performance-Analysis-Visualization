# PV Plant Performance Analysis & Visualization

## Overview
This project processes and visualizes performance data from a photovoltaic (PV) plant to evaluate its operational efficiency over time. It combines daily Performance Ratio (PR) and Global Horizontal Irradiance (GHI) data, cleans and merges the datasets, then generates a comprehensive visualization that highlights key trends and budget benchmarks.

---


## Deployment
Upload combined_file.csv in Streamlit and see the dynamic change in the graph.

## Dataset Description
- **Performance Ratio (PR):** Measures daily efficiency of the PV plant. Higher PR indicates better performance.
- **Global Horizontal Irradiance (GHI):** Measures daily solar irradiation. Higher GHI indicates sunnier days.

Data is organized in folders by parameter (`PR` and `GHI`), then further subdivided by year-month, containing daily CSV files.

---

## Features

- **Data Preprocessing:**
  - Combines all daily PR files year-wise into a single CSV file.
  - Combines all daily GHI files year-wise into a single CSV file.
  - Merges PR and GHI data into a final dataset containing Date, PR, and GHI columns.
  - Calculates a 30-day moving average for PR.
  - Dynamically computes a yearly declining budget PR line (starting at 73.9, reducing by 0.8% annually).
  - Categorizes GHI into four bins for color-coded visualization.

- **Visualization:**
  - Scatter plot of daily PR values with colors representing GHI categories:
    - GHI < 2: Navy Blue
    - 2 ≤ GHI < 4: Light Blue
    - 4 ≤ GHI < 6: Orange
    - GHI ≥ 6: Brown
  - Red line showing 30-day moving average of PR (performance trend).
  - Dark green line representing the dynamic budget PR over time.
  - Annotations for number of PR points above the budget line.
  - Summary of average PR over recent periods (7, 30, 60 days, etc.) displayed on the graph.

---

## How to Use

1. **Data Preparation:**
   - Place your raw PR and GHI data folders (with daily CSVs organized by year-month) in the project directory.
2. **Run Data Preprocessing:**
   - Use the preprocessing function to combine and merge raw data into a single dataset.
3. **Generate Visualization:**
   - Run the visualization function to create and display the performance graph.
4. **Customization:**
   - Modify the starting budget value or decay rate as needed.
   - Adjust GHI thresholds or color scheme if desired.

---



## Project Structure

│
├── data/
│ ├── PR/
│ │ ├── 2023-01/
│ │ │ ├── 2023-01-01_PR.csv
│ │ │ └── ...
│ ├── GHI/
│ ├── 2023-01/
│ │ ├── 2023-01-01_GHI.csv
│ │ └── ...
│
├── scripts/
│ ├── preprocess_data.py # Data combination and merging functions
│ ├── visualize_data.py # Visualization function
│
├── outputs/
│ ├── combined_pr.csv
│ ├── combined_ghi.csv
│ └── final_merged_data.csv
