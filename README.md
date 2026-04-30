# RouteIQ: Urban Delivery Route Optimization

## Problem Statement
Delivery startups struggle to optimise routes in dense urban areas where traffic patterns vary widely by time and locality. This project explores how historical data can reveal the most efficient delivery pathways and the factors that influence delivery times.

## Approach
This project follows the Data Science lifecycle (Question → Data → Insight) utilizing Python, NumPy, pandas, matplotlib, and seaborn:
1.  **Data Generation**: A synthetic dataset (`delivery_trips.csv`) was generated to simulate realistic urban delivery scenarios.
2.  **Data Setup & Inspection**: Data structures and arrays were handled using basic Python and NumPy operations (vectorization and broadcasting).
3.  **Data Cleaning**: Handled missing values, removed duplicates, and standardized string formats.
4.  **Exploratory Data Analysis (EDA)**: Analyzed distributions, correlations, and outliers using boxplots, histograms, scatter plots, and line plots.
5.  **Insight Generation**: Summarized key findings to answer the initial business question.

## Key Insights
*   **High Delay Areas and Times**: Distinct peaks in delivery duration occur during morning (8-10 AM) and evening (5-7 PM) rush hours. The `old_city` pickup area exhibits consistently higher base durations due to difficult navigation.
*   **Impact of Weather and Traffic**: There is a clear linear relationship between distance and duration, but higher traffic indices and adverse weather (rain/fog) add significant penalty multipliers, shifting delivery times upward.
*   **Outlier Influence**: Extreme anomalies in actual delivery durations (> 3 standard deviations) were detected, likely representing edge cases like accidents or vehicle breakdowns.

## Assumptions & Limitations
*   **Synthetic Data**: The dataset is entirely synthetic, generated using a fixed random seed.
*   **Linear/Static Assumptions**: Traffic and weather effects were modeled as static penalty multipliers. Real-world traffic is more dynamic and non-linear.
*   **No Machine Learning**: Only basic Exploratory Data Analysis and data manipulation techniques from Sprint #3 were used. Predictive modeling or advanced routing algorithms were not implemented.
*   **Uniform Distribution**: Areas and vehicle types were assigned randomly with static probabilities, which might not reflect true urban geographic distributions.

## How to Run the Project
1.  Ensure you have a Python environment with `numpy`, `pandas`, `matplotlib`, and `seaborn` installed.
2.  **Generate Data**: Run the data generation script from the project root to create the `delivery_trips.csv` dataset:
    ```bash
    python src/data_generator.py
    ```
3.  **Run Analysis**: Open the Jupyter Notebook to view the analysis:
    ```bash
    jupyter notebook notebooks/RouteIQ_analysis.ipynb
    ```
    You can execute the notebook end-to-end via `Kernel` → `Restart & Run All`.

## Folder Structure
```text
RouteIQ/
├── data/
│   ├── raw/                  # Contains the generated synthetic dataset
│   └── processed/            # For cleaned datasets (if saved)
├── notebooks/
│   └── RouteIQ_analysis.ipynb # Single complete analysis notebook
├── src/
│   └── data_generator.py     # Script that creates the synthetic data
├── outputs/
│   └── figures/              # Directory for saved plots
├── README.md                 # Project documentation
└── .gitignore                # Git ignore rules
```