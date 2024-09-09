from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
driver.maximize_window()

time.sleep(2)

electronicsMenu = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/ul/li[3]")
electronicsMenu.click()

time.sleep(2)

samsungMenu = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[3]/section[2]/div[2]/span[5]/a/div[1]")
samsungMenu.click()

time.sleep(2)

phoneMenu = driver.find_element(By.XPATH,"/html/body/div[3]/nav/div[1]/div/div/div/section/ul/li[3]")
phoneMenu.click()

time.sleep(2)

for imageNum in range(1,61):
    imageStr = "/html/body/div[3]/div[3]/div[3]/section[3]/ul/li[" + str(imageNum) + "]/div[1]/div[1]/div/a/div/div/img"
    imageFind = driver.find_element(By.XPATH,imageStr)
    imageName = "samsung image " + str(imageNum) + ".png"
    imageFind.screenshot(imageName)

time.sleep(10)

driver.close()
