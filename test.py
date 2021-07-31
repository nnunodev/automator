from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path

# chrome driver
#chromeDriver = Path('C:\ChromeDriver\chromedriver.exe')
#driver = webdriver.Chrome(chromeDriver)
driver = webdriver.Firefox()
driver.get("https://youtube.com/")
driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span').click()
driver.find_element_by_xpath('//*[@id="search"]')
