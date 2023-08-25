# Cost of Living Calculator

This program calculates and compares the purchasing power of an individual based on their salary for the years 2022 and 2023. It retrieves cost of living data from the Numbeo website for a specific city.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver

## Setup

1. Clone the repository.
2. Install the required Python packages using the following command:

   ```
   pip install -r requirements.txt
   ```

3. Download the Chrome WebDriver and place it in the project directory.

## Usage

1. Run the script `evaluate_your_rise.py`.
2. Enter your city name.
3. Enter your salary for the year 2022.
4. Enter your salary for the year 2023.

The program will retrieve cost of living data from Numbeo, calculate the purchasing power for various items, and compare the purchasing power between the two years.

## Example

```python
python evaluate_your_rise.py
```

## Output

The program will display the calculated purchasing power for various items for the years 2022 and 2023, as well as the price differences between the two years.

## Disclaimer

This program uses web scraping to retrieve data from external sources, which can be subject to change. The accuracy of the calculated values depends on the accuracy of the data provided by the website.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Remember to add a `LICENSE` file to your project directory if you choose to use a specific license for your code.

Please note that the above README.md assumes you have a `requirements.txt` file with the necessary Python packages listed, and that the script is named `evaluate_your_rise.py`. Make sure to adjust the names and paths as needed to match your project structure. Also, consider adding more details about the project, installation, and usage instructions as you see fit.
