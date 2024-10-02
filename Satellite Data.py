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
for tr in allTr:
    tdArr = []
    tds = tr.find_all('td')
    for oneTds in tds:
        tdArr.append(oneTds.text.strip())
    allData.append(tdArr)

for oneTh in allTh:
    allThText.append(oneTh.text.strip())

satelliteData = pd.DataFrame(allData,columns=[allThText],index=list(range(1,768)))

satelliteData.to_excel("Satellite Data.xlsx")
