#WebScraping
"""
from urllib.request import urlopen
import requests
"""
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap)
browser.get('http://seleniumhq.org/')

"""
def recent_25_posts(username):
    #With the input of an account page, scrape the 25 most recent posts urls
    url = "https://www.instagram.com/" + username + "/"
    browser = Firefox()
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    while len(post_links) < 25:
        links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        return post_links[:25]

recent_25_posts('space')


class WebScrapping:
    
    def __init__(self):
        self.version = 'version_01'    # instance variable unique to each instance

    def get_data_from_tag(self, tag):  
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

        r = requests.get('https://www.instagram.com/explore/tags/spacex/', headers=headers)#, proxies=proxies)
        content = r.content
        return content
       """

