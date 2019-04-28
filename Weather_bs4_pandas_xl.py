import requests
import bs4
import pandas as pd

link="https://www.meteoprog.kz/en/meteograms/Astana/"
data=requests.get(link)
#print(data.text[:300])

soup=bs4.BeautifulSoup(data.text,"html.parser")


weather_souplist = soup.find_all("tr", class_="main-weather__item-meta")
date_souplist = soup.find_all("span", class_="date")
day_souplist= soup.find_all("span", class_="day-name")

date_list=[]
day_list=[]
time_list=[]
temp_list=[]
windval_list=[]
winddir_list=[]

for j in range(3):
    for i in range(24):
        date = date_souplist[j].text
        day = day_souplist[j].text
        time = weather_souplist[(24*j)+i].td.text
        
        tempfull = weather_souplist[(24*j)+i].find("span",class_="tmp").text
        temp = int(tempfull.split("°C°")[0])
        
        wind=weather_souplist[(24*j)+i].find("td", class_="wind").text
        wind_val = int(wind.split()[0])
        
        wind_dir=weather_souplist[(24*j)+i].find("td", class_="wind")["data-name"]
        #print(day,date,time,temp,wind_val,wind_dir)

        date_list.append(date)
        day_list.append(day)
        time_list.append(time)
        temp_list.append(temp)
        windval_list.append(wind_val)
        winddir_list.append(wind_dir)
        

df = pd.DataFrame({"Date":date_list,"Day":day_list,"Time":time_list,
                   "Temp":temp_list,"Wind Speed": windval_list,
                   "Wind Dir":winddir_list})

xl = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
df.to_excel(xl)
xl.save()

#average temperature
tod_temp = sum(df.loc[0:24,"Temp"])/24 #today
tom_temp = sum(df.loc[24:48,"Temp"])/24 #tommorow
aft_tom_temp = sum(df.loc[48:72,"Temp"])/24 #day after tommorow

print("Today temp:", round(tod_temp,2))
print("Tommorrow temp:", round(tom_temp,2))
print("Day after tomorrow temp:", round(aft_tom_temp,2))



