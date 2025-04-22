from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

ACCOUNT_EMAIL = "rahulkumarb83@gmail.com"
ACCOUNT_PASSWORD = "Rahul@7781032790###linkedln"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=India")

# Sign in
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))).click()
except:
    try:
        driver.find_element(By.CSS_SELECTOR, 'a.nav__button-secondary').click()
    except Exception as e:
        print("Couldn't find sign-in link:", e)

# Login
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    email_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, "password")
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
except Exception as e:
    print("Login error:", e)

# input("Solve CAPTCHA and press Enter to continue...")

# try:
#     easy_apply = driver.find_element(By.ID,"jobs-apply-button-id")
#     easy_apply.click()
#     print("Easy Apply button clicked!")
# except Exception as e:
#     print("Couldn't find Easy Apply button:", e)

# Sign in
# try:
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))).click()
# except:
#     try:
#         driver.find_element(By.CSS_SELECTOR, 'a.nav__button-secondary').click()
#     except Exception as e:
#         print("Couldn't find sign-in link:", e)
# try:
#     # Wait until the 'Easy Apply' button is present and clickable
#     easy_apply_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
#     )
#     easy_apply_button.click()
#     print("Easy Apply button clicked successfully.")
# except Exception as e:
#     print("Error: Unable to locate or click the 'Easy Apply' button.")
#     print(f"Exception: {e}")

#Locate the apply button
# time.sleep(5)
# apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
# apply_button.click()

# #If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
# if phone.text == "":
#     phone.send_keys("+919528305652")

# #Submit the application
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()
# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        # if phone.text == "":
        #     phone.send_keys('')

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()