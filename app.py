from bs4 import BeautifulSoup

content = []
with open("favorites_9_1_20.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

# clearing empty p tags
for x in soup.findAll():
    if len(x.get_text(strip=True)) == 0:
        x.extract()

tags = soup.find_all(["h1", "h3", "a"])

def parentLinks():
    parent = []
    body = soup.find('body')
    parentDl = body.findAll('dl', recursive=False)
    parentDT = parentDl[0].findAll('dt', recursive=False)
    for dt in parentDT:
        aC = dt.find_all('a')
        for el in aC:
            if el.text:
                parent.append({'title': el.text, 'link': el['href']})
    return parent

for i in range(len(tags)):
    if tags[i].name == "h1":
        parent = parentLinks()
        if parent:
            content.append({"title": "General", "data": parent})
    elif tags[i].name == "h3":
        parent = []
        title = tags[i].text
        dl = tags[i].find_next('dl', recursive=False)
        dt = dl.findAll('dt', recursive=False)
        for dt in dt:
            aC = dt.find_all('a')
            for el in aC:
                if el.text:
                    parent.append({'title': el.text, 'link': el['href']})
        content.append({'title': title, 'data': parent})

print(content)
