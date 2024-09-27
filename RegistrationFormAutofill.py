import random
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

password = "pass" + str(random.randint(100,999))

details = ["","","genericmail123@gmail.com",password,password,"John Doe","Doe","1302141314416","Male","","Home123","PAKISTAN","KARACHI","23215"
           ,"Home456","","Punjab","Islam","03343421295"]
divDetails = ["","22","Aug","1991"]

driver = webdriver.Chrome()
driver.get("https://smartcareers.pk/register.aspx")
driver.maximize_window()

time.sleep(2)

for xpathNum in range(2,19):
    if xpathNum != 15:
        if (xpathNum <= 9 and xpathNum >= 8) or (xpathNum >= 11 and xpathNum <= 12) or (xpathNum >= 16 and xpathNum <= 17):
            if (xpathNum == 9):
                for divNum in range(1,4):
                    selectorBox = driver.find_element(By.XPATH,"/html/body/form/div[3]/section/div/div/div[2]/div[" + str(xpathNum) + "]/div[" + str(divNum) + "]/select")
                    selectorBoxSelec = Select(selectorBox)
                    selectorBoxSelec.select_by_visible_text(divDetails[divNum])

            else:
                selectorBox = driver.find_element(By.XPATH,"/html/body/form/div[3]/section/div/div/div[2]/div[" + str(xpathNum) + "]/div/select")
                selectorBoxSelec = Select(selectorBox)
                selectorBoxSelec.select_by_visible_text(details[xpathNum])

        else:
            selectTBox = driver.find_element(By.XPATH,"/html/body/form/div[3]/section/div/div/div[2]/div["+ str(xpathNum) +"]/div/input")
            selectTBox.click()
            selectTBox.send_keys(details[xpathNum])


        time.sleep(2)

    print(xpathNum)

time.sleep(100)

driver.close()
