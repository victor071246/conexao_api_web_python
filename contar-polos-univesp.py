from html.parser import HTMLParser
from urllib.request import urlopen, Request

class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos +=1

    def num_polos(self):
        return self.n_polos
    