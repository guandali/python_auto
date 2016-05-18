from selenium import webdriver
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
chromedriver = "/usr/local/bin/chromeDriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


# go to the google home page
driver.get("https://www.reddit.com/")

# the page is ajaxy so the title is originally this:
print ("Title is"+driver.title)

# find the element that's name attribute is q (the google search box)
#inputElement = driver.find_element_by_name("q")

# type in the search
#inputElement.send_keys("cheese!")
username_inputElement = driver.find_element_by_name('j_username')
password_inputElement = driver.find_element_by_name('j_password')
# submit the form (although google automatically searches now without submitting)
username_inputElement.send_keys('lli@gmail.com')
password_inputElement.submit('thisispassword')

try:

    driver.find_element_by_name("login-form").submit()

   # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))


    print (driver.title)

finally:
    driver.quit()