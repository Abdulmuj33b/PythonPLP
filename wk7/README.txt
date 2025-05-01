
## Overview
This Python script performs comprehensive exploratory data analysis (EDA) with automated data cleaning, statistical analysis, and professional visualizations. Works with both the built-in Iris dataset and custom CSV files.

## Features
- **Smart Data Handling**
  - Auto-detects numerical/categorical columns
  - Handles missing values (fills with mean)
  - Automatic date parsing for time-series

- Advanced Statistics
  - Descriptive stats (mean, std, min/max)
  - Variance calculation
  - Grouped aggregations

- Publication-Quality Visualizations
  - 4 integrated plot types with custom styling
  - Automatic annotations
  - High-resolution export (300 DPI)

## Usage
### Basic (Iris Dataset)
```
use_iris = True  # Default configuration
```

### Custom CSV Analysis
1. Place your data as `custom_data.csv` in same folder
2. Set:
```
use_iris = False
```
3. Script automatically:
   - Detects date columns
   - Handles missing values
   - Adapts visualizations to your data structure

## Outputs
1. Console Output
   - Data preview
   - Statistical summaries
   - Group analyses

2. Visualizations
   - Saved as `enhanced_analysis.png` with:
     - Time-series line plot
     - Comparative bar chart
     - Distribution histogram
     - Relationship scatter plot

## Customization Options
```python
# Style Customization
sns.set_style("whitegrid")  
custom_palette = sns.color_palette("husl", 3)

# Analysis Add-ons
stats.loc['variance'] = df.var()  # Added to describe()

# Plot Enhancements
plt.savefig(dpi=300, bbox_inches='tight')  # High-res export
```

## Requirements
- Python 3.6+
- Libraries:
  ```
  pip install pandas matplotlib seaborn scikit-learn
  ```

## Error Handling
- File not found
- Missing value detection
- Type conversion errors

## Example Output
```
=== Using Custom CSV Dataset ===
First 5 rows:
   sepal_length  sepal_width  species
0           5.1          3.5   setosa
...

=== Enhanced Statistics ===
       sepal_length  sepal_width
count    150.000000   150.000000
mean       5.843333     3.057333
std        0.828066     0.435866
variance   0.685694     0.189979
```

Author: Your Name  
Version: 1.1  
License: PLP (Free for reuse)
