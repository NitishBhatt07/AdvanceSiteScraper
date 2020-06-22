from bs4 import BeautifulSoup
import requests

links = []
actual_links = []
link_titles = []

main_links_url = []   # main open links
main_links_titles = []  #main open titles

def get_overflow_titles(query):
    url = 'https://stackoverflow.com/search?q='+query
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchors = soup.find_all('a',class_='question-hyperlink')

    # links with anchor <a> tag list ########
    for link in anchors:
        links.append(link)
    # geting link title with stating A and Q list ######
    for link in links:
        link_titles.append(link.get_text())
    # geting only main useful tiles list #########
    for title in link_titles:
        if title[3] == ":":
            main_links_titles.append(title[4:])
    return main_links_titles

def get_overflow_links(query):
    url = 'https://stackoverflow.com/search?q='+query
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchors = soup.find_all('a',class_='question-hyperlink')

    # links with anchor <a> tag list ########
    for link in anchors:
        links.append(link)
    # links without anchor tag list ##########
    for link in anchors:
        actual_links.append(link.get('href'))
    # geting only main useful links list #########
    for link in actual_links:
        if link[-1] == "s":
            main_links_url.append(link)
    return main_links_url













        
    
    
