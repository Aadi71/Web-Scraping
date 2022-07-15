import requests
from bs4 import BeautifulSoup


URL = "https://www.emsisoft.com/ransomware-decryption-tools/free-download"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

time = soup.find_all(class_ = "Post__header__time")
title = soup.find_all(class_ = "Post__header__title")
desc = soup.find_all(class_ = "Post__body")
links = [i.find("a")["href"] for i in soup.find_all('div', attrs={'class': 'Post__download'})]

print("Web Scraping the www.emsisoft.com: \n")

for i in range(len(title)):
    print("Time and Version: "+ time[i].text)
    print("Name of the  tool: " + title[i].text, end = "")
    print("Description of the tool: " + desc[i].text, end = "")
    print("Download Link: " + "https://www.emsisoft.com/ransomware-decryption-tools/" + links[i])
    print("\n")
