from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://dgcs.gos.pk/index.php?#colleges-table")
driver.maximize_window()

time.sleep(2)

regionMenu = driver.find_element(By.ID, "region")
regionSelect = Select(regionMenu)
regionSelect.select_by_visible_text("KARACHI")

time.sleep(2)

districtMenu = driver.find_element(By.ID, "district")
districtSelect = Select(districtMenu)
districtSelect.select_by_visible_text("KARACHI EAST")

time.sleep(2)

for xpathNum in range(1,34):
    xpathString = "/html/body/section[5]/div/div[4]/table/tbody/tr[" + str(xpathNum) +"]/td[3]"
    collegeName = driver.find_element(By.XPATH,xpathString)
    print(collegeName.text)

time.sleep(5)

driver.close()
