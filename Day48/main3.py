from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

f_name = driver.find_element(By.NAME,value="firstname")
f_name.send_keys("Rahul Kumar")

l_name = driver.find_element(By.NAME,value='lastname')
l_name.send_keys("Bhagat")

# e_mail = driver.find_element(By.NAME,value='email')
# e_mail.send_keys('rahul.12345@gmail.com')

# s_button = driver.find_element(By.CSS_SELECTOR,value="form button")
# s_button.click()
print("Form submited sucessfully")