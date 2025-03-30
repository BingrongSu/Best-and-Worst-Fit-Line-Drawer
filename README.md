
# Best and Worst Fit Line Drawer

Visualize the best and worst fit lines.

## Description
This repository contains tools for performing simple data analysis, specifically focusing on drawing the best and worst fit lines for a given set of data points. The tools are implemented in Python.

## Features
- **Best Fit Line**: Calculate and draw the best fit line for a given set of data points.
- **Worst Fit Lines**: Calculate and draw two worst fit lines for a given set of data points.
- **Visualization**: Visualize the data points, error bars along with the best and worst fit lines.

## Installation
To use these tools, you can either use Python to run it yourself, or install the .exe file in [Releases](https://github.com/BingrongSu/Best-and-Worst-Fit-Line-Drawer/releases/tag/files).

## Usage
Here is an example of how to use the tools in this repository:

1. **Prepare your data**: Ensure your data is split by space (eg. "3 5 6 9").
2. **Prompt**: Prompt in x-data, y-data, x-error-bars, and y-error bars separately. Ensure they have the same number of components. A "Guess gradient" is required: input a positive or negative number which represents the trend of your data is increasing or decreasing.

Example input:
```
1 2 3 4 5 6 7
2.1 2.9 4.4 5.1 5.8 7.2 8
0.2 0.2 0.2 0.3 0.4 0.1 0.2
0.3 0.3 0.5 0.3 0.3 0.2 0.2
114514
```

Example Result:
![Result](https://github.com/BingrongSu/Best-and-Worst-Fit-Line-Drawer/blob/main/Example.png)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

## License
This project is licensed under the CC0 License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please contact [Bingrong Su](https://github.com/BingrongSu).
