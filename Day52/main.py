from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

USERNAME = "t93718427@gmail.com"
PASSWORD = "Rahul@7781032790###"
SIMILAR_ACCOUNT = 'mumbaiindians'

class InstaFollower():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url=url)
        sleep(4.2)

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()
        
        username = self.driver.find_element(By.NAME,value="username")
        password = self.driver.find_element(By.NAME,value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2.1)
        password.send_keys(Keys.ENTER)

        sleep(4.3)
        save_login_prompt = self.driver.find_element(By.XPATH,value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        sleep(3.7)
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()




    # def find_followers(self):
    #     sleep(5)
    #     self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

    #     sleep(5.2)
    #     modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
    #     modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
    #     for i in range(10):
    #         # In this case we're executing some Javascript, that's what the execute_script() method does.
    #         # The method can accept the script as well as an HTML element.
    #         # The modal in this case, becomes the arguments[0] in the script.
    #         # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
    #         self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    #         sleep(2)

    def find_followers(self):
        # Go to the user profile
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(5)

        # Click on the followers link to open the modal
        try:
            followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
            followers_link.click()
        except NoSuchElementException:
            print("Could not find followers link.")
            return

        sleep(5)

        # Wait for modal and scroll through it
        try:
            modal = self.driver.find_element(By.XPATH, "//div[@role='dialog']")
            # Locate the inner scrollable container of the followers list (adjusted target)
            # scrollable_area = self.driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
            print("Scrollable area found inside modal.")
            for _ in range(10):  # Scroll multiple times
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
                print("1")
                sleep(2)
        except NoSuchElementException:
            print("Modal not found.")




    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._ap30 button" )
        print("follow")
        for button in all_buttons:
            try:
                button.click()
                print("clicked")
                sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                print("cancel")



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
