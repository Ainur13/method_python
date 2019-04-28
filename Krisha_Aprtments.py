import bs4 
import requests

link = "https://krisha.kz/arenda/kvartiry/"

city=input("City? ")
city = city.lower()
link = link + city + "/"

room = input("Room? ")
link = link + "?das[live.rooms]=" + room

#add other filters....

data = requests.get(link)

soup = bs4.BeautifulSoup(data.text, "html.parser")
taglist=soup.find_all("a", class_="a-card__title")

print("\nLast 10 apartments:\n")
for i in range(10):
    print(str(i+1)+".",taglist[i].text)
    print("https://krisha.kz"+taglist[i]["href"])
    print()
