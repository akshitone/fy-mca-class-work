from bs4 import BeautifulSoup
import requests

search = input("Enter movie name: ").replace(" ", "+")

moviesmod = requests.get(f"https://moviesmod.co/?s={search}")
reqzone = requests.get(f"https://reqzone.com/search?query={search}")
extramovies = requests.get(f"https://extramovieshub.shop/?s={search}")

moviesmod_doc = BeautifulSoup(moviesmod.text, "html.parser")
reqzone_doc = BeautifulSoup(reqzone.text, "html.parser")
extramovies_doc = BeautifulSoup(extramovies.text, "html.parser")

# print(reqzone_doc)


links_moviesmod = moviesmod_doc.find_all(
    "article", class_="latestPost excerpt")
links_reqzone = reqzone_doc.find_all(
    "div _ngcontent-wlp-c135", {"class": "grid-label"})

links_extramovies = extramovies_doc.find_all(
    "h3", {"class": "gridshow-grid-post-title"})


# print(links_extramovies)

# print(links_moviesmod)

for link in links_moviesmod:
    print(link.a['title'])
    print(link.a['href'])
    print("\n")


# for link in links_reqzone:
#     print(link.header.h1.a.text)
#     print(link.header.h1.a['href'])
#     print("\n")

for link in links_extramovies:
    print(link.text)
    print(link.a['href'])
    print("\n")
