from bs4 import BeautifulSoup
import requests
import re
import csv
import random

res = requests.get('https://www.ssa.gov/oact/babynames/decades/century.html')
soup = BeautifulSoup(res.text, 'html.parser')

tds = soup.find_all('td')
tds = tds[1:-2]


for td in tds:
    match = re.search('^([^0-9]*)$', str(td))
    if match:
        name = re.sub(r'(<td>|</td>)', '', str(td))

with open('people.csv', 'w+', newline='') as file:
    fields = ['Name', 'Age']
    csvwriter = csv.DictWriter(file, fieldnames=fields)
    csvwriter.writeheader()

    for td in tds:
        match = re.search('^([^0-9]*)$', str(td))
        if match:
            name = re.sub(r'(<td>|</td>)', '', str(td))
            csvwriter.writerow({'Name': name, 'Age': random.randint(10, 80)})
