from html.parser import HTMLParser

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])
    
parser = myParser()
for _ in range(int(input())):
    parser.feed(input())
