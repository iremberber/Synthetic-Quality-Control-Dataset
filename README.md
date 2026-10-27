# Synthetic Quality Control Dataset for Plastic Components

## Overview

This project focuses on generating a synthetic quality control dataset for plastic component manufacturing using Python.

The dataset simulates a visual inspection process for 300 plastic components produced by two injection molding machines. It is designed as a foundation for quality engineering analysis, defect monitoring, and data visualization.

**Note:** All data is synthetically generated for educational and portfolio purposes. It does not represent actual production records.

## Project Objectives

- Generate a structured quality control dataset.
- Simulate production and inspection timestamps.
- Record machine, production cycle, cavity, and shift information.
- Represent multiple visual defect categories.
- Prepare data for defect analysis and quality performance monitoring.

## Dataset Description

The dataset contains 300 simulated parts produced using two injection molding machines: `IM01` and `IM02`.

Each record represents one part and includes production information, inspection timing, and visual defect indicators.

### Production and Inspection Fields

| Column | Description |
|---|---|
| Part ID | Unique identifier assigned to each part |
| Machine No | Injection molding machine identifier |
| Cycle No | Production cycle number |
| Cavity No | Mold cavity identifier |
| Shift | Production shift (A or B) |
| Production Time | Simulated production timestamp |
| Inspection Start | Time when visual inspection begins |
| Inspection Duration (sec) | Simulated inspection duration |
| Inspection End | Time when inspection is completed |

### Visual Defect Categories

The dataset includes 10 defect categories:

1. Scratches and impact marks
2. Surface marks
3. Dust, dirt, and foreign objects
4. Flash
5. Incomplete printing
6. Stains
7. Fogging
8. Cracks and breakage
9. Part noise
10. Faint marking

Each defect category is represented by a Boolean value indicating whether the defect is present (`True`) or absent (`False`).

## Tools and Technologies

- **Python** for dataset generation
- **NumPy** for random data generation
- **pandas** for data manipulation and Excel export
- **Microsoft Excel** for dataset inspection
- **Power BI** as a planned tool for visualization

## Methodology

1. Define production parameters, including machines, cycles, and cavities.
2. Generate part identifiers and simulated production timestamps.
3. Simulate inspection durations and sequential inspection scheduling.
4. Assign synthetic single-defect and multiple-defect cases.
5. Export the resulting dataset to Excel for further analysis.

## Planned Analysis

The dataset is intended to support the following future analyses:

- Overall defect rate and defect frequency
- Pareto analysis to identify the most frequent defect categories
- Machine-based and shift-based quality comparisons
- Quality performance dashboards in Power BI
- Data-driven interpretation of potential quality improvement opportunities

These analyses will be developed in subsequent project stages.

## Limitations

- The dataset is synthetic and does not reflect real factory measurements.
- Defect assignments are randomly generated using predefined proportions.
- Observed patterns should not be interpreted as evidence of actual manufacturing root causes.
- The simulated inspection schedule represents a simplified inspection process.

## Project Status

**Current stage:** Dataset generation and Excel export completed.

**Next stage:** Data validation, exploratory analysis, Pareto analysis, and visualization.

## Author

Industrial Engineering graduate interested in quality engineering, manufacturing processes, and data-driven problem solving.
