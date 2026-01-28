import matplotlib.pyplot as plt

# Simple data - days of the week and temperatures
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperatures = [72, 68, 75, 80, 78]

# Create the plot
plt.plot(days, temperatures)

# Add labels and title
plt.xlabel('Day of Week')
plt.ylabel('Temperature (°F)')
plt.title('Weekly Temperature Forecast')

# Display the plot
plt.show()
