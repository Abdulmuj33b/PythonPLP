Sales Data Analysis Script Documentation
Overview
This Python script analyzes sales data from a CSV file (sales_data.csv), calculates key metrics, saves insights to a text file (sales_summary.txt), and generates visualizations (sales_trends.png).

Features
Data Analysis
Calculates total revenue
Identifies the best-selling product (by quantity sold)
Finds the highest revenue day

Output
Saves results in sales_summary.txt
Prints insights in a user-friendly format
Visualization (Bonus)
Bar chart: Daily revenue trends
Pie chart: Product sales distribution

Requirements
Python 3.x

Libraries:
pip install pandas matplotlib
Input File Format (sales_data.csv)
Date (YYYY-MM-DD)	Product	Quantity Sold	Revenue ($)
2025-03-01	Laptop	5	5000
2025-03-01	Mouse	15	300
Output Files
sales_summary.txt

    Total Revenue: $38,700
    Best-Selling Product: Mouse (25 units sold)
    Highest Sales Day: 2025-03-07 ($7,500)
    sales_trends.png

Left: Daily revenue bar chart
Right: Product sales pie chart

How to Run
Save your sales data as sales_data.csv.

Execute the script:
      python sales_analysis.py

Check generated files:

  sales_summary.txt (text insights)
  sales_trends.png (visual trends)

Customization
Modify CSV columns: Adjust column names in the script if needed.
Change visuals: Edit matplotlib settings for different chart styles.

Author & License
Author: Abidoye Abdulmujeeb
License:PLP (Free for reuse)
