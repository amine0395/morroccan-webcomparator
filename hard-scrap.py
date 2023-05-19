import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import playground

path="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
def scrape_marjane(marjmall_url,query):
    columns = {'name': [], 'price': [], 'img url': []}
    driver.get(marjmall_url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol")))
    search = element.find_elements(By.CLASS_NAME, "product-item-info")
    if search:
        a = 999999.0
    for item in search:
        name = item.find_element(By.CLASS_NAME, "product-item-link")
        link = item.find_element(By.CLASS_NAME, "product-item-link").get_attribute('href')
        item = item.find_element(By.CLASS_NAME, "price-wrapper")
        price = item.get_attribute('data-price-amount')
        if playground.matches_query(name,query):
            if float(price) < a:
                a=float(price)
                columns = {'name': [], 'price': [], 'img url': []}
                columns['name'].append(name.text)
                columns['price'].append(price)
                columns['img url'].append(link)
    driver.quit()
    return columns

