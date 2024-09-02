from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
driver.maximize_window()

time.sleep(2)

searchBar = driver.find_element(By.XPATH,"/html/body/div[3]/div/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div/div/input[1]")
searchBar.send_keys("Smart Watches")
searchBtn = driver.find_element(By.XPATH,"/html/body/div[3]/div/header/table/tbody/tr/td[4]/input")
searchBtn.click()

time.sleep(2)

"/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[3]/div"

for num in range(2,62):
    stringX = "/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[" + str(num) + "]/div"
    searchItem = driver.find_element(By.XPATH,stringX)
    print(searchItem.text)


time.sleep(10)

driver.close()
