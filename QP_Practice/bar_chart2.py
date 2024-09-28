import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 20, 15, 25]

# Create bar graph
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Bar Graph Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Add grid lines
plt.grid(True, linestyle='-.', alpha=0.7)

# # Add annotations
# for i, value in enumerate(values):
#     plt.text(i, value + 0.5, str(value), ha='center')

# Add legend
plt.legend(['Values'])

# Show the plot
plt.show()
