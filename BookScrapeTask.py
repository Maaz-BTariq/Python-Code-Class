from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
driver.maximize_window()
allBooks = []

for pages in range(1,51):
    bookArr = []
    for books in range(1,21):
        bookArr = []
        bookInfo = "/html/body/div[1]/div/div/div/section/div[2]/ol/li[" + str(books) + "]/article/h3/a"
        bookFind = driver.find_element(By.XPATH,bookInfo)
        bookArr.append(bookFind.get_attribute("title"))
        bookArr.append(bookFind.get_attribute("href"))
        allBooks.append(bookArr)
    time.sleep(2)
    if not pages == 50:
        if pages == 1:
            nextButton = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section/div[2]/div/ul/li[2]/a")
        else:
            nextButton = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section/div[2]/div/ul/li[3]/a")
        nextButton.click()

time.sleep(10)

bookDataframe = pd.DataFrame(allBooks,columns=["Title","URL"],index=list(range(1,1001)))
print(bookDataframe)

driver.close()
