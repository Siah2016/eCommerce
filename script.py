from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
# Book Mark - "div" class= "clo-sm-4"
# Name - "a" class= "title"
# Price - "h4" class= "pull-right price"
# Specification - "p" class= "description"
# Number of Review - "p" class= "pull-right"
file = open("laptops.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name", "Price", "Specifications", "Number of Reviews"])
browser_driver = Service("chromedriver.exe")
scraper = webdriver.Chrome(service=browser_driver)
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

cookies = WebDriverWait(scraper, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'acceptCookies')))
cookies.click()


while True:
        Laptops = scraper.find_elements(By.CLASS_NAME, "thumbnail")
        
        for laptop in Laptops:
                data = []
                name = laptop.find_element(By.CLASS_NAME, "title").text
                price = laptop.find_element(By.TAG_NAME, "h4").text[1:]
                specification = laptop.find_element(By.CLASS_NAME, "description").text
                number_of_review = laptop.find_element(By.CLASS_NAME, "ratings").text[0:2]
                data.append(name)
                data.append(price)
                data.append(specification)
                data.append(number_of_review)
                writer.writerow(data)
        try:
                scraper.find_element(By.PARTIAL_LINK_TEXT, "»").click()
        except NoSuchElementException:
                break
file.close()
scraper.quit()