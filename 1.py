from bs4 import BeautifulSoup

def parentLinks():
    content = {}
    with open("favorites_9_1_20.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    # clearing empty p tags
    for x in soup.findAll():
        if len(x.get_text(strip=True)) == 0:
            x.extract()

    body = soup.find('body')
    parentDl = body.findAll('dl', recursive=False)
    parentDT = parentDl[0].findAll('dt', recursive=False)
    for dt in parentDT:
        aC = dt.find_all('a')
        for el in aC:
            if el.text is not None:
                content.update({"General": el})

    return content

parentLinks()