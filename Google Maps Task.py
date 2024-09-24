import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@24.9666676,67.1298671,15z?entry=ttu&g_ep=EgoyMDI0MDkxNi4wIKXMDSoASAFQAw%3D%3D")
driver.maximize_window()

searchBar = driver.find_element(By.ID,"searchboxinput")
searchBar.send_keys("Hospitals in Karachi")
searchBar.send_keys(Keys.ENTER)
time.sleep(10)

actions = ActionChains(driver)

for index in range(3,191,2):
    locationFind = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[" + str(index) + "]/div/a"
    locationLocate = driver.find_element(By.XPATH,locationFind)
    print(locationLocate.get_attribute("aria-label"))

    scrollbar = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div')

    actions.move_to_element(scrollbar).click_and_hold().perform()
    actions.move_to_element(scrollbar).send_keys("\ue00f").perform()


driver.close()
