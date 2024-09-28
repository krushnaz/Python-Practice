import matplotlib.pyplot as plt

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [23, 45, 56, 32]
values2 = [15, 30, 45, 60]

# Plot the bar graph
plt.bar(categories, values1, label='Group 1')
plt.bar(categories, values2, label='Group 2', alpha=0.5)

# Add decorations
plt.title('Comparison of Groups')
plt.xlabel('Categories')
plt.ylabel('Values')        
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.show()
