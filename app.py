# from aiohttp import web
# from bs4 import BeautifulSoup

# def listToString(s):      
#    str1 = " " 
#    return (str1.join(s)) 

# def handle():

#    with open("index.html") as file:
#       soup = BeautifulSoup(file, features='lxml')

#       for allA in soup.find_all('a'):
#          print(allA.get_attribute_list('href')[0] )
#          for i in allA.find_all_previous('h3'):
#             print (i.get_text())

      
      # for dt_a in soup.find_all(['dt', 'a']):
      #    if dt_a.find('a'):
      #       title = dt_a.find_previous('h3').text
      #       for dl_h3 in dt_a.parent.find_parents('dl'):
      #             if dl_h3.find('h3'):
      #                if title != dl_h3.find('h3').text:
      #                   title = dl_h3.find('h3').text + ' - ' + title
      #                   print(title, '---',dt_a.find('a')['href'].split("//")[-1].split("/")[0].split('?')[0])


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
      for h in tags[i].find_all_previous('h3'):
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


# {
#    "Bookmarks": [
#       "70+ Best Comfort Food Recipes - Easy Ideas for Comfort Foods",
#       "100 Easy Comfort Food Recipes that Come Together Quick | Taste of Home",
#       "Discover the Best eBooks, Audiobooks, Magazines, Sheet Music, and More | Scribd",
#       "DeviantArt - Discover The Largest Online Art Gallery and Community"
#    ],
#    "Bookmarks - Favorites bar":[
#       "Google",
#       "reddit: the front page of the internet",
#       "Stack Overflow - Where Developers Learn, Share, & Build Careers",
#    ],
#    "Bookmarks - Favorites bar - recipes":[
#       "Comfort Food Recipes | Allrecipes",
#       "100 Easy Comfort Food Recipes | Easy Comfort Food Recipes | Food Network",
#       "50+ Comfort Food Recipes | MyRecipes",
#       "Comfort Food Recipes to Curl Up With | Bon Appétit",
#       "101 Best Classic Comfort Food Recipes | Southern Living",
#    ],
#    "Bookmarks - Favorites bar - recipes - vegan":[
#       "40 Mouthwatering Vegan Dinner Recipes! | Feasting At Home",
#       "85 Best Vegan Recipes - Love and Lemons",
#       "54 Best Vegan Recipes - Easy Vegan Dinner Ideas You'll Love",
#    ]
# }

print("Hello world")
print("checking this file")