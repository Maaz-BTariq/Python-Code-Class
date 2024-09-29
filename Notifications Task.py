import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.dgcs.gos.pk/udocs/#/notifications")
driver.maximize_window()
time.sleep(2)
table = driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div/div/div/div/div[2]/div[2]/div/div/div")

actions = ActionChains(driver)

arr = []

for pageSelec in range(25):
    for index in range(32):
        actions.move_to_element(table).click_and_hold().perform()
        actions.move_to_element(table).send_keys("\ue00f").perform()

        for finder in range(1,11):
            onelineArr = []
            for divNum in range(1,7):
                if divNum != 6:
                    stringFind = "/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[" + str(finder) +"]/div[" + str(divNum) + "]"
                    dataFind = driver.find_element(By.XPATH, stringFind).text
                    onelineArr.append(dataFind)
                else:
                    stringFind = "/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[" + str(finder) +"]/div[6]/a"
                    dataFind = driver.find_element(By.XPATH,stringFind)
                    href = dataFind.get_attribute("href")
                    onelineArr.append(dataFind)

            if not onelineArr in arr:
                arr.append(onelineArr)

    if pageSelec != 24:
        nextButton = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div[2]/div/div[3]/button[2]")
        nextButton.click()
        actions.move_to_element(table).click_and_hold().perform()
        actions.send_keys(Keys.PAGE_UP*100).perform()

    time.sleep(1)
time.sleep(20)

print(arr)

arrDataframe = pd.DataFrame(arr,columns=["Sr No","Notification No","Subject","Category","Date","Download HREF"])
arrDataframe.to_excel("Information from Website.xlsx")

driver.close()
