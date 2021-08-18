from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#white while it loads the content
try:
    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )
    
    titles = contents.find_elements_by_tag_name("video-title")
    for title in titles:
        tit = title.find_elements_by_id("title-wrapper")
        print(tit.text)
finally:
    driver.quit()


