from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
# chrome driver
chromeDriver = Path('C:\ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(chromeDriver)
# firefox driver
#driver = webdriver.Firefox()

driver.get("https://youtube.com/")
driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span').click()
searchBox = driver.find_element_by_xpath('//input[@id="search"]')
searchBox.send_keys('Muse')

searchButton = driver.find_element_by_xpath(
    '//*[@id="search-icon-legacy"]').click()

time.sleep(10)
driver.quit()