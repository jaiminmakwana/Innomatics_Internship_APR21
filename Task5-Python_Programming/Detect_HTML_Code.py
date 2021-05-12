from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


html = '\n'.join([input() for i in range(int(input()))])
parser = myHTMLParser()
parser.feed(html)
parser.close()