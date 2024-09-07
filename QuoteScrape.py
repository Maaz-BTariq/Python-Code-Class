from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")
driver.maximize_window()

time.sleep(2)

allQuotes = []

for index in range(1,11):
    quotesAndTags = []
    tagFind = "/html/body/div[1]/div[2]/div[2]/span[" + str(index) + "]/a"
    tagFinder = driver.find_element(By.XPATH,tagFind)
    quotesAndTags.append(tagFinder.text)
    tagFinder.click()
    time.sleep(2)
    for index2 in range(1,11):
        quoteFind = "/html/body/div[1]/div[2]/div[1]/div[" + str(index2) + "]/span[1]"
        try:
            quoteFinder = driver.find_element(By.XPATH,quoteFind)
            quotesAndTags.append(quoteFinder.text)
        except:
            pass
    allQuotes.append(quotesAndTags)


time.sleep(5)

driver.close()

columnsQuote = ["Tag"]
for tempIndex in range(1,11):
    columnsQuote.append("Quote" + str(tempIndex))

indexDF = list(range(1,11))

quotesDataframe = pd.DataFrame(allQuotes,columns=columnsQuote,index=indexDF)

print(quotesDataframe)
