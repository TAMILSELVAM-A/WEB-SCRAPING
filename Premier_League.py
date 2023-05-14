import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set the path to the chromedriver executable
chromedriver_path = '/path/to/chromedriver'

# Set up the Selenium driver
driver = webdriver.Chrome(service=Service(executable_path=chromedriver_path), options=chrome_options)

# Load the webpage
driver.get("https://www.premierleague.com/tables")

# Wait for the dynamic content to load
# You may need to adjust the wait time based on the page load speed
driver.implicitly_wait(5)

# Get the updated page source after dynamic content loading
page_source = driver.page_source

# Close the Selenium driver
driver.quit()

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Points_Table'
sheet.append(['Poistion','Team','Matches', 'Won', 'Drawn', 'Lost', 'Gf', 'Ga','Gd','Points'])

try :
  # Continue with BeautifulSoup for parsing the page source and extracting data
  soup = BeautifulSoup(page_source, 'html.parser')

  #  Find and process the table data
  points_table = soup.find('tbody', class_="tableBodyContainer isPL").find_all("tr")

  for table in points_table :
      position_element = table.find('span', class_='value')
      position = position_element.text if position_element else "N/A"

      team_name_element = table.find('span', class_='long')
      team_name = team_name_element.text if team_name_element else "N/A"

      team_td = table.find('td', class_='team')
      if team_td:
        data_td = team_td.find_next_siblings('td', limit=8)
        if len(data_td) >= 8:
            Played, Won , Drawn, Lost, Gf, Ga, Gd, Points = [td.get_text(strip=True) for td in data_td]
            # print(position,team_name,Played, Won, Drawn, Lost, Gf, Ga,Gd,Points)
            sheet.append([position,team_name,Played, Won, Drawn, Lost, Gf, Ga,Gd,Points])

except Exception as e:
       print(e)

excel.save("Points_table.xlsx")

