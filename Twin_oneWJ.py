import requests
from bs4 import BeautifulSoup
import re
import csv
import json

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return [], [], []

    soup = BeautifulSoup(response.text, 'html.parser')

    names = []
    for name_tag in soup.find_all(['h1', 'h2', 'h3']):
        names.append(name_tag.get_text(strip=True))

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
    
    # Regex for Bangladeshi phone numbers
    phone_numbers = re.findall(r'(?:\+8801|01)\d{9}', response.text)

    return names, emails, phone_numbers


def save_to_csv(names, emails, phone_numbers, url, filename="Hello World.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone Number", "URL"])

        max_len = max(len(names), len(emails), len(phone_numbers))
        for i in range(max_len):
            writer.writerow([names[i] if i < len(names) else '', 
                             emails[i] if i < len(emails) else '', 
                             phone_numbers[i] if i < len(phone_numbers) else '', 
                             url])  

    print(f"Data extraction complete from {url} and saved to CSV.")


def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jfile:
        data = json.load(jfile)
        
    with open(csv_file, 'w', newline='', encoding='utf-8') as cfile:
        writer = csv.writer(cfile)
        
        if isinstance(data, list):
            if data:
                headers = data[0].keys()
                writer.writerow(headers)
                for item in data:
                    writer.writerow(item.values())
        else:
            writer.writerow(data.keys())
            writer.writerow(data.values())
    
    print(f"Data extraction from {json_file} has been successfully completed to {csv_file}.")

choice = input("What is your choice? For Website, press W. For JSON file, press J: ").strip().upper()

if choice == 'W':
    url = input("Please enter Website URL: ")
    names, emails, phone_numbers = scrape_website(url)
    save_to_csv(names, emails, phone_numbers, url)
elif choice == 'J':
    json_file = input("Enter the JSON file path: ")
    csv_file = input("Enter a CSV file name: ")
    json_to_csv(json_file, csv_file)
else:
    print("Invalid choice. Data extraction incomplete. Try again.")
