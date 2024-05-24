from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('htpp://www.uol.com.br')

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = MyParser()
parser.feed(html)