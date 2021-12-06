# Beautifulsoup


# sudo apt-get install python3-bs4
# pip install beautifulsoup4


from bs4 import BeautifulSoup
import requests
import pickle

url = 'https://teploradost.com.ua'

#
# soup = BeautifulSoup(response.text, 'html.parser')
headers = {
    'content-type': 'text',
    'Authorization': 'Token uher438fjaoer8u3or38wuro3ro8u'
}

if __name__ == '__main__':
    session = requests.Session()
    # print(session.headers)
    session.headers.update(headers)
    # print(session.headers)
    # response = requests.get(url, headers=headers)
    response = session.get(url)
    category_links = []
    if response.status_code == 200:
        # print('Ok')
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.title)
        c = 0
        for category_link in soup.find_all('img', class_='lazyloads'):
            c += 1
            # print(category_link.parent.get_text())
            print(category_link.parent['href'])
            category_links.append(category_link.parent['href'])
            # if c > 3:
            #     break
    # print(c)
    print(len(category_links))

    with open('category_links.pkl', 'wb') as f:
        pickle.dump(category_links, f)



