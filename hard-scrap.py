from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
def marjane():
    driver.get("https://www.marjanemall.ma/catalogsearch/result/index/?p=2&q=xiaomi+redmi&product_list_order=most_viewed")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol")))
        search = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol")
        print("-------------------------------")
        print(search)
        i=0;
        for item in search:
            print("-------------------------------")
            print(item)
            price=item.find_element("/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol/li["+i+"]/div/div/div[2]/div[1]/span/span/span")
            i+=1
            print(price.text)
    except:
        driver.quit()
marjane()
