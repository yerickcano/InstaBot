#WebScraping

from urllib.request import urlopen
import requests

class WebScrapping:
    
    def __init__(self):
        self.version = 'version_01'    # instance variable unique to each instance

    def get_data_from_tag(self, tag):  
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

        r = requests.get('https://www.instagram.com/explore/tags/spacex/', headers=headers)#, proxies=proxies)
        content = r.content
        return content

