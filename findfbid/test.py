import json
import urllib.request
from bs4 import BeautifulSoup
url = "https://www.facebook.com/anhngoc.5312"
f = urllib.request.urlopen(url)
content = f.read()
soup = BeautifulSoup(content, "html.parser")
temp = soup.find("meta", attrs={'property': 'al:android:url'})
temp = str(temp).split('\" ')[0]
temp = temp.split('/')[-1]
data = {}
data['key'] = temp
json_data = json.dumps(data)
print(json_data)


