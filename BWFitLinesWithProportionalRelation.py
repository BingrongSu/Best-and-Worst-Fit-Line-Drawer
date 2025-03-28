import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_fit(x, a):
    return a * x

def get_float_list(prompt):
    while True:
        try:
            # Split the input string by spaces and convert each element to float
            values = [float(x) for x in input(prompt).split()]
            return np.array(values)
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

# Sample data with x and y error-bars
x_data = np.array(get_float_list("X values: "))
y_data = np.array(get_float_list("Y values: "))
x_err = np.array(get_float_list("X Uncertainties: "))
y_err = np.array(get_float_list("Y Uncertainties: "))

# Perform curve fitting
popt, pcov = curve_fit(linear_fit, x_data, y_data, sigma=y_err, absolute_sigma=True)
a_best = popt[0]

# Calculate the worst fit lines
trendUp = int(input("Guess gradient: ")) > 0
worstFit1, worstFit2 = 0, 0
for i in range(x_data.size):
    # gradient has minimum absolute value
    ax = 0
    bx = x_data[i] - x_err[i]
    ay = 0
    by = y_data[i] + (y_err[i] if trendUp else -y_err[i])
    m = (by-ay)/(bx-ax)
    # see if the line passes through all the error bars
    canFit = True
    for k in range(x_data.size):
        if not(y_data[k] - y_err[k] <= m*(x_data[k]-x_err[k]) <= y_data[k] + y_err[k]) and not(y_data[k] - y_err[k] <= m*(x_data[k]+x_err[k]) <= y_data[k] + y_err[k]):
            canFit = False
            break
    if canFit:
        if worstFit1 == 0 or abs(worstFit1[0]) > abs(m):
            worstFit1 = m

for i in range(x_data.size):
    # gradient has minimum absolute value
    ax = 0
    bx = x_data[i] + x_err[i]
    ay = 0
    by = y_data[i] - (y_err[i] if trendUp else -y_err[i])
    m = (by-ay)/(bx-ax)
    # see if the line passes through all the error bars
    canFit = True
    for k in range(x_data.size):
        if not(y_data[k] - y_err[k] <= m*(x_data[k]-x_err[k]) <= y_data[k] + y_err[k]) and not(y_data[k] - y_err[k] <= m*(x_data[k]+x_err[k]) <= y_data[k] + y_err[k]):
            canFit = False
            break
    if canFit:
        if worstFit2 == 0 or abs(worstFit2[0]) > abs(m):
            worstFit2 = m

print(worstFit1)
print(worstFit2)

# Generate x values for plotting
x_fit = np.linspace(min(x_data)-1, max(x_data)+1, 100)

# Calculate y values for the best fit line and worst fit lines
y_best_fit = linear_fit(x_fit, a_best)

# Plot the data points with error bars
plt.errorbar(x_data, y_data, xerr=x_err, yerr=y_err, fmt='o', label='Data points', ms = 4, capsize=4)

# Plot the best fit line
plt.plot(x_fit, y_best_fit, label=f'Best fit line: y={round(a_best, 5)}x', color='blue')

if worstFit1 != 0:
    y_extra_line01 = worstFit1 * x_fit
    plt.plot(x_fit, y_extra_line01, label=f'Worst fit line: y={round(worstFit1, 5)}x', color='orange', linestyle='-.')
if worstFit2 != 0:
    y_extra_line02 = worstFit2 * x_fit
    plt.plot(x_fit, y_extra_line02, label=f'Worst fit line: y={round(worstFit2, 5)}x', color='red', linestyle='-.')



# Add labels and title
plt.xlabel('V/V')
plt.ylabel('K')
plt.title('Relationship Between K and V0')
plt.legend()

# Show the plot
plt.show()
