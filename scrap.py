import shodan
import requests
from bs4 import BeautifulSoup
import csv

# Shodan API key
SHODAN_API_KEY = 'your_shodan_api_key'
api = shodan.Shodan(SHODAN_API_KEY)

# Function to find websites hosted on the same IP
def find_websites_on_ip(ip_address):
    try:
        result = api.host(ip_address)
        websites = [item.get('hostnames') for item in result.get('data', [])]
        return websites
    except Exception as e:
        print(f"Error finding websites for IP {ip_address}: {e}")
        return []

# Function to scrape personal data (name, phone, email) from a website
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Custom logic to find name, phone, and email (adjust according to website structure)
        name = soup.find('span', {'class': 'name'}).text if soup.find('span', {'class': 'name'}) else 'N/A'
        phone = soup.find('span', {'class': 'phone'}).text if soup.find('span', {'class': 'phone'}) else 'N/A'
        email = soup.find('a', {'href': lambda x: x and x.startswith('mailto:')}).text if soup.find('a', {'href': lambda x: x and x.startswith('mailto:')}) else 'N/A'

        return name, phone, email
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Function to store scraped data in a CSV file
def store_data(data):
    with open('scraped_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Main function to run the process
def main(ip_address):
    # Step 1: Get websites hosted on the same IP
    websites = find_websites_on_ip(ip_address)
    
    if not websites:
        print(f"No websites found for IP {ip_address}")
        return

    # Step 2: Scrape data from each website
    for website in websites:
        website_url = f'http://{website[0]}'  # Get the first hostname (you may modify this)
        print(f"Scraping website: {website_url}")
        
        data = scrape_website(website_url)
        if data:
            print(f"Data from {website_url}: Name: {data[0]}, Phone: {data[1]}, Email: {data[2]}")
            store_data(data)

# Run the script for a given IP address
if __name__ == '__main__':
    target_ip = 'YOUR_TARGET_IP'  # Replace with the target IP address
    main(target_ip)
