import matplotlib.pyplot as plt
import numpy as np

# Generate random data (replace this with your own data)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [25, 18, 16, 12, 29]

# Calculate cumulative percentage
total = sum(values)
cumulative_percentage = np.cumsum(values) / total * 100

# Create a Pareto chart
fig, ax1 = plt.subplots()

# Bar chart
ax1.bar(categories, values, color='blue')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Frequency', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Line chart (cumulative percentage)
ax2 = ax1.twinx()
ax2.plot(categories, cumulative_percentage, color='red', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Display the Pareto chart
plt.title('Pareto Chart')
plt.show()
