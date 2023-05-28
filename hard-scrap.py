import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import playground
import unicodedata





path="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
def scrape_marjane(marjmall_url,query):
  columns = {'name': [], 'price': [], 'img url': []}
  driver.get(marjmall_url)
  if (driver.current_url == marjmall_url):
   try:
    WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/div/div[3]/ol")))
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
    return columns
   except TimeoutException:
      return columns
def  scrape_avito(avito_url ,query):
    columns = {'name': [], 'price': [], 'img url': []}
    driver.get(avito_url)
    if(True):
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div[6]/div[1]/div/div[2]")))
            search = element.find_elements(By.CLASS_NAME, "sc-jejop8-0.epNjzr")
            a=99999999
            for item in search:
                name=item.find_element(By.CLASS_NAME, "sc-jejop8-20.gsYzZU")
                link=item.find_element(By.CLASS_NAME, "cYNgZe").get_attribute('href')
                try:
                    price_element = item.find_element(By.CSS_SELECTOR,
                                                      "span.sc-1x0vz2r-0.bpfcIG.sc-jejop8-18.dfevBq span[dir='auto']")
                    price = price_element.text
                    if playground.matches_query(name, query):
                        print("true 1")
                        numeric_price = float(unicodedata.normalize("NFKD", price).replace(" ", ""))
                        if numeric_price < a:

                            a = numeric_price
                            columns = {'name': [], 'price': [], 'img url': []}
                            columns['name'].append(name.text)
                            columns['price'].append(price)
                            columns['img url'].append(link)
                except:
                    continue
            return columns
        except:
            return columns

def scrape_electroplanet(ecplanet_url,query):
    columns = {'name': [], 'price': [], 'img url': []}
    driver.get(ecplanet_url)
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div/div/div/div/div[2]/div[2]/div[3]/div[1]/ol")))
    search = element.find_elements(By.CLASS_NAME, "product-item-info")
    if bool(search):
        a=999999999.0
    for item in search:
        name = str(item.find_element(By.CLASS_NAME, "brand").text)+" "+str(item.find_element(By.CSS_SELECTOR, "html body#html-body.page-products.page-with-filter.catalogsearch-result-index.page-layout-2columns-left div.page-wrapper main#maincontent.page-main div.columns.col2-layout div.container div.row div.main_wrapper.clearfix div.main-col.col-lg-10.col-md-10 div.column.main div.search.results.Product_listing_ div.category-product.products.wrapper.grid.products-grid ol.products.list.items.product-items.row li.item.product.product-item.col-lg-3.col-md-3.col-sm-4.col-xs-12 div.product-item-info div.item-inner div.product.details.product-item-details.box-info div.product.name.product-item-name.product-name a.product-item-link span.ref").text)
        link = item.find_element(By.CLASS_NAME, "product-item-link").get_attribute('href')
        price = item.find_element(By.CLASS_NAME, "price").text
        if playground.matches_query1(name,query):
            if float(price.replace(" ", "")) < a:
                a=float(price.replace(" ", ""))
                columns = {'name': [], 'price': [], 'img url': []}
                columns['name'].append(name)
                columns['price'].append(price.replace(" ", ""))
                columns['img url'].append(link)
    driver.quit()
    return columns
