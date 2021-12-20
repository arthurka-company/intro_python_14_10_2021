# Beautifulsoup


# sudo apt-get install python3-bs4
# pip install beautifulsoup4


from bs4 import BeautifulSoup
import requests

url = 'https://teploradost.com.ua'

response = requests.get(url)

print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.text)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.h2)
# print(soup.p)
# print(soup.a)

# print(soup.find_all('a'))
# print(soup.find_all('h2'))

for item in soup.find_all('h2'):
    print(item.text)
    print(item.get_text())


print(soup.get_text())


