#BOT
from InstaParser import InstaParser
from WebScrapping import WebScrapping

def iniciar():
    print("WebScrapping started\n")
    ws = WebScrapping()
    insta = InstaParser()
    insta.parse(ws.get_data_from_tag('spacex'))
    print("Web info aquired\n")
    print("Parsing started\n")
    print(insta.getTitle())
    #print(insta.getImagesDivsList())
    #print(insta.soup)
    print("Parsing completed\n")
iniciar()