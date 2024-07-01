import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the results page
url = 'https://results.eci.gov.in'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant data table (adjust the selector as needed)
table = soup.find('table', {'class': 'table-class-name'})  # Replace 'table-class-name' with the actual class name

# Extract the table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the table rows
rows = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    columns = [col.text.strip() for col in columns]
    if columns:
        rows.append(columns)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv('election_results.csv', index=False)

print("Scraping complete. Data saved to 'election_results.csv'.")
