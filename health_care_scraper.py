import requests
from bs4 import BeautifulSoup
import re
import csv


URL = 'https://www.hnhbhealthline.ca/listServicesDetailed.aspx?id=10363&region=Hamilton'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='mainLeft')
health_elems = results.find_all('td', class_='b10')


file = open('pswhamilton.csv','w')
writer = csv.writer(file)

writer.writerow(['Name', 'Link', 'Details'])

for health_elem in health_elems:
    title_elem = health_elem.find('a')

    add_elem = health_elem.find('span', class_='regtext')

    if title_elem != None:
        placeName = title_elem.text.strip()
        placeLink = f"https://www.hnhbhealthline.ca/{title_elem.get('href')}".strip()

    if add_elem != None:
        addNum = add_elem.text.strip()

        writer.writerow([placeName,placeLink,addNum])

    
file.close()





# print(results.prettify())
