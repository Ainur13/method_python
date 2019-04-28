import requests

# API выглядит как link1+название_города+link2
link1 = "http://api.openweathermap.org/data/2.5/weather?q="
link2 = "&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d"

city=input("Enter city name: ")

link = link1+city+link2 # лепим новую рабочую ссылку
data = requests.get(link) # делаем на нее запрос

temp = data.json()['main']['temp'] # вытаскиваем температуру
country = data.json()['sys']['country'] # вытаскиваем страну
pogoda = data.json()['weather'][0]['main'] # вытаскиваем саму погоду

print(country, city)
print("Today is", pogoda)
print("Temperature:", temp)

