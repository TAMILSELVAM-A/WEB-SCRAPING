# WEB-SCRAPING
Scraped the English Premier League points table using Python's Beautiful Soup and Selenium.

# English Premier League Points Table Scraper
This Python script utilizes Beautiful Soup and Selenium to scrape the English Premier League points table. Beautiful Soup is a powerful library for web scraping in Python that allows us to parse HTML and XML documents, making it easy to extract specific data from web pages. Selenium, on the other hand, is a tool commonly used for web automation. In this project, we combine the strengths of both libraries to automate the process of fetching the dynamically loaded points table data from a website.

# Installation
To run this script, please ensure you have the following dependencies installed:

Python (version 3.0 or above)
Beautiful Soup library
Selenium library

You can install the dependencies by running the following command:

pip install beautifulsoup4 selenium

Make sure to also download the appropriate web driver for Selenium, compatible with your preferred web browser.

# Usage
Clone this repository to your local machine or download the source code files.

Open the script in a Python-compatible IDE or editor.

Configure the web driver path in the script to match the location of the web driver on your system.

Run the script using the following command:

python scrape_premier_league_table.py

The script will automatically navigate to the website, use Selenium to fetch the dynamically loaded points table data, and then parse it using Beautiful Soup. The results will be displayed in a formatted manner.

# Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments
The Beautiful Soup library: https://www.crummy.com/software/BeautifulSoup/
The Selenium library: https://www.selenium.dev/
