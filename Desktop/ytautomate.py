from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

keyword= input("Song Name : ")
driver = webdriver.Chrome()
#driver.maximize_window()

#wait = WebDriverWait(driver, 3)
#presence = EC.presence_of_element_located
#visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/results?search_query={}'.format(str(keyword)))



href = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
link = href.get_attribute('href')

driver.get('https://ytmp3.cc/en13/')
search_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form/input[1]')
search_box.send_keys(link)
search_box.send_keys(Keys.ENTER)

driver.implicitly_wait(5)
download_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
download_button.click()
