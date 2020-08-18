#BOThttps://medium.com/swlh/tutorial-web-scraping-instagrams-most-precious-resource-corgis-235bf0389b0c
from InstaParser import InstaParser
from WebScrapping import WebScrapping

def iniciar():
    ws = WebScrapping()
    insta = InstaParser()
    insta.parse(ws.get_data_from_tag('spacex'))
    print(insta.getTitle())
    #print(insta.getImagesDivsList())
    print(insta.soup)

iniciar()