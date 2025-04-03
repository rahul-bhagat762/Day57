from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_count = driver.find_element(By.ID,value='articlecount')
# temp = article_count.text.split(" ")
# print("Article Count:",temp[3])
# print("Editor Count:",temp[0])


# article_count = driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
# # print(article_count.text)
# article_count.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT,value="tributary")
# all_portals.click()

# sending the "search" keyboard input to 
search = driver.find_element(By.NAME,value="search")
search.send_keys("Python",Keys.ENTER)
search.send_keys()


# driver.quit()