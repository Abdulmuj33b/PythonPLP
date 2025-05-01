import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# 1. Calculate total revenue
total_revenue = df['Revenue ($)'].sum()

# 2. Find best-selling product (by quantity)
best_selling = df.loc[df['Quantity Sold'].idxmax()]['Product']
best_selling_qty = df['Quantity Sold'].max()

# 3. Find day with highest sales (by revenue)
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
daily_sales = df.groupby('Date')['Revenue ($)'].sum()
highest_day = daily_sales.idxmax().strftime('%Y-%m-%d')
highest_day_revenue = daily_sales.max()

# Save results to file
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue:,}\n")
    f.write(f"Best-Selling Product: {best_selling} ({best_selling_qty} units sold)\n")
    f.write(f"Highest Sales Day: {highest_day} (${highest_day_revenue:,})\n")

# Print insights
print("=== Sales Insights ===")
print(f"Total Revenue: ${total_revenue:,}")
print(f"Best-Selling Product: {best_selling} ({best_selling_qty} units sold)")
print(f"Highest Sales Day: {highest_day} (${highest_day_revenue:,})")

# Bonus: Visualization
plt.figure(figsize=(10, 5))

# Plot daily revenue
plt.subplot(1, 2, 1)
daily_sales.plot(kind='bar', color='skyblue')
plt.title('Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')

# Plot product quantities
plt.subplot(1, 2, 2)
product_sales = df.groupby('Product')['Quantity Sold'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Product Sales Distribution')

plt.tight_layout()
plt.savefig('sales_trends.png')
plt.show()
