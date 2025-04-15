from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


PROMISED_DOWN = 150
PROMISED_UP = 10
# CHROME_DRIVER_PATH = '' 
TWITTER_EMAIL = 'rahulkbhagat1'
TWITTER_PASSWORD = 'Rahul@7781032790###'

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        continue1 = self.driver.find_element(By.XPATH,value='''//*[@id="onetrust-accept-btn-handler"]''')
        continue1.click()
        sleep(3)
        go = self.driver.find_element(By.CSS_SELECTOR,value='.start-button a')
        go.click()
        sleep(60)

        self.down = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        # print(self.down)
        self.up = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(self.up)
    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        
        sleep(3)
        id  =  self.driver.find_element(By.XPATH,value='''//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input''')
        id.click()
        id.send_keys(TWITTER_EMAIL)
        sleep(3)
        
        next_button = self.driver.find_element(By.XPATH,value='''//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span''')
        next_button.click()
        sleep(3)

        # some_other = self.driver.find_element(By.XPATH,value='''''')
        
        password = self.driver.find_element(By.NAME, "password")

        # self.driver.find_element(By.XPATH,value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input''')
        # # password.click()
        sleep(2)
        password.send_keys(TWITTER_PASSWORD)
        
        sleep(2)
        # login_click = self.driver.find_element(By.XPATH,value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button''')
        # login_click.click()
        
        # sleep(3)
        
        # # sleep(2)
        # # login_button = self.driver.find_element(By.XPATH, '//span[text()="Log in"]/ancestor::div[@role="button"]')
        # # login_button.click()

        # login_button = self.driver.find_element(By.CLASS_NAME,value='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')
        login_button = self.driver.find_element(By.XPATH, '//button[normalize-space()="Log in"]')
        sleep(2)
        login_button.click()
        print("its clicked")
        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div''')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()

        sleep(2)
        self.driver.quit()



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()



