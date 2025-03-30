# Best and Worst Fit Line Drawer

Simple Data Analysis Tools

## Description
This repository contains tools for performing simple data analysis, specifically focusing on drawing the best and worst fit lines for a given set of data points. The tools are implemented in Python.

## Features
- **Best Fit Line**: Calculate and draw the best fit line for a given set of data points.
- **Worst Fit Line**: Calculate and draw the worst fit line for a given set of data points.
- **Visualization**: Visualize the data points along with the best and worst fit lines.

## Installation
To use these tools, you need to have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage
Here is an example of how to use the tools in this repository:

1. **Prepare your data**: Ensure your data is in a format that can be processed by the script (e.g., a CSV file with two columns: x and y).
2. **Run the script**: Use the provided Python scripts to calculate and visualize the best and worst fit lines.

```python
# Example usage
from line_drawer import draw_best_fit_line, draw_worst_fit_line

data = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)]
draw_best_fit_line(data)
draw_worst_fit_line(data)
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Social Media Preview
![Social Media Preview](assets/social_preview.png)

## Contact
For any questions or inquiries, please contact [Bingrong Su](https://github.com/BingrongSu).
