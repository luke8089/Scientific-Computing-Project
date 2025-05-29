import matplotlib.pyplot as plt
# Temperature readings
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# Plotting
plt.plot(days, temperatures, marker='o')
plt.title('Weekly Temperature Readings')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
