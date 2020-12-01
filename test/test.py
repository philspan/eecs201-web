from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "/mnt/c/Users/pspan/OneDrive - Umich/Fall 2020/EECS 201/eecs201-web/test/chromedriver.exe"
DOMAIN = "https://philspan.github.io/eecs201-web/blog"

class InvalidPageError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return "InvalidPageError: {0}".format(self.message)
        else:
            return "InvalidPageError"

driver = webdriver.Chrome(PATH)
driver.get(DOMAIN)
print(driver.title)

# Get link elements
links = driver.find_elements(By.TAG_NAME,'a')
blogPosts = []
for linkElement in links:
    blogPosts.append(linkElement.get_attribute("href"))

# Go to each link and print 
for link in blogPosts:
    try:
        driver.get(link)
        if ("404" in driver.title):
            raise InvalidPageError
        print(driver.title)
        driver.back()
    except InvalidPageError as e:
        # Catch 404 Error
        print("{e}: This link does not lead to any page yet.")

# Close webdriver
driver.close()