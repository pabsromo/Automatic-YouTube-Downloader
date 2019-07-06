from bs4 import BeautifulSoup
import requests

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')

getPlaylistLinks('https://www.youtube.com/playlist?list=PLU6vjRCwipdd0TcvjUc-O_lrugeOzU_v_')
