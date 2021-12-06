import requests

from bs4 import BeautifulSoup
import pickle


pages = ['', '?page=2', '?page=3', '?page=4']
urls = [
    'https://teploradost.com.ua',
]
headers = {
    'content-type': 'text',
    # 'user-agent': 'Mozilla / 5.0(X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko)'
    #               ' Ubuntu Chromium / 71.0.3578.98 Chrome / 71.0.3578.98'
    #               ' Safari / 537.36'
}


if __name__ == '__main__':
    s = requests.Session()
    result = []

    r = s.get(urls[0], headers=headers)
    if r.status_code == 200:
        print('OK')
        soup = BeautifulSoup(r.text, 'html.parser')

        for i in soup.find_all('img', class_='lazyloads'):
            print(i.parent['href'])
            result.append(i.parent['href'])
    pickle.dump(result, open('urls.pkl', 'wb'))

