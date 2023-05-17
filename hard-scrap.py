from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
def marjane():
    driver.get("https://www.marjanemall.ma/catalogsearch/result/index/?p=2&q=xiaomi+redmi&product_list_order=most_viewed")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol")))
    search = element.find_elements(By.CLASS_NAME,"product-item-info")
    for item in search:
        name=item.find_element(By.CLASS_NAME,"product-item-link").text
        print(name)
        link=item.find_element(By.CLASS_NAME,"product-item-link").get_attribute('href')
        print(link)
        item = item.find_element(By.CLASS_NAME,"price-wrapper")
        price=item.get_attribute('data-price-amount')
        print(price)
    driver.quit()
marjane()
