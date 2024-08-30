from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as mplp
import requests as rq
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
openWeb = rq.get(url).text
webFind = bs(openWeb,"html.parser")
all_tables = webFind.select("#main_table_countries_today tbody tr")
mainData = []

for table in all_tables:
    count = 0
    all_td = table.find_all("td")
    allDataList = []
    for td in all_td:
        allDataList.append(td.getText())
    mainData.append(allDataList)

mainDataSliced = []
for index in range(len(mainData)):
    if (index >= 7 and index <= 238) or index == len(mainData)-1:
        mainDataSliced.append(mainData[index])



all_th = webFind.select('#main_table_countries_today thead tr th')

headings = []
for th in all_th:
    headings.append(th.text)

dataFrame = pd.DataFrame(mainDataSliced,columns=headings)

print(dataFrame)

mplp.bar(dataFrame["Country,Other"],dataFrame["TotalCases"])
mplp.grid()
mplp.title("Total Cases of Covid in Countries")
mplp.xlabel("Country,Other")
mplp.ylabel("Total Cases")
mplp.show()
