#BS4 parser
from bs4 import BeautifulSoup

class InstaParser:
    def __init__(self):
        self.version = 'parser_version1'    # instance variable unique to each instance
        self.soup = ''
    
    def parse(self, htmlToParse):
        soup = BeautifulSoup(htmlToParse,features="lxml")
        self.soup = soup
    
    def getTitle(self):
        return self.soup.title
        
    def getDivs(self):
        return self.soup.d
        
    def getImagesDivsList(self):
        imagesList = self.soup.findAll('div', attrs={'class':'Nnq7C weEfm'})
        return imagesList
    