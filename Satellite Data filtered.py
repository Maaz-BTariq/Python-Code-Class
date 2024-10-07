import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.satellite-calculations.com/Satellite/satellitelist.php?AMATEURALLNEAR"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find('table',id='main')
allTh = table.find_all('th')
allTr = table.find_all('tr')
print(f"Number of rows: {len(allTr)}")

allData = []
allThText = []
collection = False
skipFirst = False

for tr in allTr:
    tdArr = []
    tds = tr.find_all('td')
    if skipFirst == True:
        if tds[2].text.strip() == "EXPRESS-AM7":
            collection = True
        elif tds[2].text.strip() == "EUTELSAT 36D":
            collection = False
    else:
        skipFirst = True

    if collection:
        for tdsNum in [0,1,2,3,4,13,21,30]:
            tdArr.append(tds[tdsNum].text.strip())
        allData.append(tdArr)

for thNum in [0,1,2,3,4,13,21,30]:
    allThText.append(allTh[thNum].text.strip())

satelliteData = pd.DataFrame(allData,columns=[allThText],index=list(range(1,18)))

satelliteData.to_excel("Satellite Data.xlsx")
