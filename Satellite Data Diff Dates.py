import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://www.satellite-calculations.com/11parameter/ephemeris/separationlist.php?53.3772668N/2.8813544W/0.19589988708496092/59987/171/60/-1.0E-8?0/0/59915#google_vignette"
driver.get(url)
driver.maximize_window()

time.sleep(2)
driver.refresh()
time.sleep(2)

allData = []
allDate = []
allTime = []
firstTime = True

table = driver.find_element(By.CSS_SELECTOR,'table#main')
rows = table.find_elements(By.TAG_NAME,'tr')
heading = table.find_elements(By.TAG_NAME,'th')
headingText = []

for i in heading:
    headingText.append(i.text.strip())


for oneRow in rows:
    if oneRow != rows[0]:
        columns = oneRow.find_elements(By.TAG_NAME,'td')
        dateAndTime = columns[1].text.strip()
        dateAndTimeArr = dateAndTime.split(" ")
        if (dateAndTimeArr[0] not in allDate and dateAndTimeArr[1] in allTime) or firstTime:
            rowData = []
            for oneColumn in columns:
                rowData.append(oneColumn.text.strip())
            allData.append(rowData)
            allDate.append(dateAndTimeArr[0])
            allTime.append(dateAndTimeArr[1])
            if firstTime:
                firstTime = False

time.sleep(2)


driver.close()

satelliteData = pd.DataFrame(allData,columns=headingText,index=list(range(1,len(allData)+1)))

satelliteData.to_excel("Satellite Data Diff Dates.xlsx")
