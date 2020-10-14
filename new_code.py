from bs4 import BeautifulSoup

content = {}
with open("favorites_9_1_20.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# @tags contains all <a> and <h3> tags where <h3> tag is category of bookmarks and <a> is the links of bookmarks.
tags = soup.find_all(["h3", "a"])

for i in range(len(tags)):
    if tags[i].name == "h3":  # if the tag is equal to <h3>, means it's a category of bookmarks
        title = tags[i].get_text()
        #   print(title, '->', tags[i].find_all_previous('h3'))
        for h in tags[i].find_all_previous(['h1', "h3"]):
            title = h.text + ' - ' + title
        links_in_category = []
        i += 1
        while tags[i].name != "h3":  # adding all <a> tag text in list while we are not getting next <h3> tag
            links_in_category.append(tags[i].get_text())
            i += 1
            if i == len(tags):
                break
        content.update({title: links_in_category})  # updating dictionary with category of bookmarks and, bookmarks

print(content)
