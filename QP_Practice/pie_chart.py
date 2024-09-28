import matplotlib.pyplot as plt

# Sample data
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # explode the 2nd slice (B)

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)

# Add title
plt.title("Sample Pie Chart")

# Add legend
plt.legend(loc='upper right')

# Add annotation
plt.annotate('Sample Annotation', xy=(0.5, 0.5), xytext=(0.6, 0.6),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add text
plt.text(-1.5, 1.5, 'Sample Text', fontsize=12, color='red')

# Add circle for donut chart
circle = plt.Circle((0, 0), 0.6, color='white')
plt.gca().add_artist(circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show plot
plt.show()
