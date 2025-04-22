from selenium import webdriver
from selenium.webdriver.common.by import By
#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

# price_dollar = driver.find_element(By.TAG_NAME,value='')
# # price_cents = driver.find_element(By.CLASS_NAME,value='a-price-fraction')
# print(f"Upcoming Events\n {price_dollar.text}")

event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

print("📅 Upcoming Events:")
for date, name in zip(event_dates, event_names):
    print(f"🔹 {date.text} - {name.text}")





# driver.close() #this is used to close only single tab
# driver.quit() #this option is used to cloase all the tabs of the browser