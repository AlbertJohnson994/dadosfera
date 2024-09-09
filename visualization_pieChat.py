import matplotlib.pyplot as plt

# Sample data
data = {
    'month_year': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', 
                   '2023-06', '2023-07', '2023-08', '2023-09', '2023-10'],
    'total_sales': [15000, 18000, 17000, 21000, 19000, 22000, 17500, 16500, 23000, 18500]
}

# Extract month names and sales values
labels = data['month_year']
sales = data['total_sales']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sales, labels=labels, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title for the pie chart
plt.title('Distribution of Total Sales Over 10 Months')

# Show the pie chart
plt.show()
