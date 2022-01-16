
import requests
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/"
subject = str(input("[*] Enter your subject >> "))
url = url + subject
req = requests.get(url)

soup = bs(req.content, "html.parser")
wiki = soup.find_all("p")

for i in range(10):
	if wiki[i].text == "\n":
		pass
	else:
		print(wiki[i].text)
		break

