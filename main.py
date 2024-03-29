import re
import requests
from bs4 import BeautifulSoup
import hard_scrap
# Function to check if a product name matches the search query
def matches_query(name, query):
    name_words = name.text.strip().lower().split()
    z = name_words if len(name_words) < len(query) else query
    i=0
    for x in z:
        if name_words[i]!=x or query[i]!=x:
            return False
        i+=1
    return True
def matches_query1(name, query):
    name_words = name.lower().split()
    z = name_words if len(name_words) < len(query) else query
    i=0
    for x in z:
        if name_words[i]!=x or query[i]!=x:
            return False
        i+=1
    return True

def extract_price(price_str):
    # remove all non-numeric characters from the string
    numeric_str = ''.join(filter(str.isdigit, price_str))
    # convert the resulting string to a float and return it
    return float(numeric_str) / 100
def convert_to_float(value_str):
    # Replace any comma with a period
    value_str = value_str.replace(",", ".")
    # Remove any non-numeric characters
    value_str = "".join(filter(str.isdigit, value_str))
    # Convert the string to a float and divide by 100
    return float(value_str) / 100
def extract_price1(price):
    if price is None:
        return None
    price_str = price.replace("Dhs", "").strip()
    pattern = r'\d[\d\,\.]*'
    match = re.search(pattern, price_str)
    if match is None:
        return None
    numeric_str = match.group().replace(',', '')
    return float(numeric_str)
def assemble(query):
    b=""
    for a in query:
        b=b+a+" "
    return b
# Main function to scrape Jumia and CosmosElectro for products
def scrape_jumia(jumia_url, base_jumia_url, query, choice):
  if choice=='1':
        category = "Phones & Tablets/Mobile Phones"
  elif choice == '2':
        category = "Accessories"
  elif choice == '3':
        category = "Phones & Tablets/Accessories/Smart Watches"
  elif choice == '4':
        category = "Electronics/Television & Video"
  elif choice == '5':
        category = "Computing/Computers & Accessories/Computers & Tablets/"

  columns = {'name': [], 'price': [], 'img url': []}
  try:
    jumia_r = requests.get(jumia_url)
    jumia_soup = BeautifulSoup(jumia_r.content, "html.parser")
    jumia_anchors = jumia_soup.find('div', {'class': '-paxs row _no-g _4cl-3cm-shs'}).find_all('article', {
          'class': 'prd _fb col c-prd'})
    if jumia_anchors:
        a = 9999999

    for anchor in jumia_anchors:
        img = anchor.find('a', href=True)["href"]
        cat = anchor.find('a', href=True)["data-category"]
        name = anchor.find('a').find('div', {'class': 'info'}).find('h3', {'class': 'name'})
        price = float(extract_price(anchor.find('a').find('div', {'class': 'info'}).find('div', {'class': 'prc'}).text))
        if matches_query(name, query) and str(category) in str(cat):
            if a > price:
                a = price
                columns = {'name': [], 'price': [], 'img url': []}
                columns['name'].append(name.text)
                columns['price'].append(price)
                columns['img url'].append(base_jumia_url + str(img))

    return columns
  except:
      return columns


def scrape_cosmos(cosmos_url,query):
    columns = {'name': [], 'price': [], 'img url': []}
    cosmos_r = requests.get(cosmos_url)
    cosmos_soup = BeautifulSoup(cosmos_r.content, "html.parser")
    cosmos_anchors = cosmos_soup.find_all(class_='col-xl-2 col-lg-4 col-md-4 col-sm-6 col-6')
    if cosmos_anchors:
        a = 999999999
    for anchor in cosmos_anchors:
        img = anchor.find('a', href=True)["href"]
        price = float(extract_price1(anchor.find(class_='ps-product__price').text))
        name = anchor.find(class_='ps-product__title').string
        if matches_query(name, query):
            if a > price:
                a=price
                columns = {'name': [], 'price': [], 'img url': []}
                columns['name'].append(name)
                columns['price'].append(price)
                columns['img url'].append(img)
    return columns
def scrape_bousfiha(bousfiha_url,query):
    columns = {'name': [], 'price': [], 'img url': []}
    bousfiha_r = requests.get(bousfiha_url)
    bousfiha_soup = BeautifulSoup(bousfiha_r.content, 'html.parser')
    bousfiha_anchors = bousfiha_soup.find_all(class_="product-container")
    if bousfiha_anchors:
        a=9999999
    for anchor in bousfiha_anchors:
        img = anchor.find('a', href=True)["href"]
        price = float(convert_to_float(anchor.find(class_='price').string))
        name = anchor.find(class_='product-title').find('a', href=True).text
        if str(assemble(query).lower()) in name.lower():
            if a>=price:
                a=price
                columns = {'name': [], 'price': [], 'img url': []}
                columns['name'].append(name)
                columns['price'].append(price)
                columns['img url'].append(img)
    return columns
def scrape_avito(avito_url,query):
    columns = {'name': [], 'price': [], 'img url': []}
    avito_r= requests.get(avito_url)
    avito_soup = BeautifulSoup(avito_r.content, 'html.parser')
    try:
        avito_anchors = avito_soup.find_all(class_="sc-jejop8-0 epNjzr")
        if avito_anchors:
            a=2000000000
        for anchor in avito_anchors:
            img=anchor.find('a',href=True)["href"]
            price= float(convert_to_float(anchor.find(class_='sc-1x0vz2r-0 bpfcIG sc-jejop8-18 dfevBq').string))
            print(img,"  \prix:  ",price)
    except:
        return


def scrape_products(query,choice):
    columns = {'name': [], 'price': [], 'img url': []}
    columns1 = {'name': [], 'price': [], 'img url': []}
    base_jumia_url='https://www.jumia.ma'
    jumia_url = base_jumia_url+'/catalog/?q=' + '+'.join(query) + '#catalog-listing&page='
    cosmos_url = 'https://www.cosmoselectro.ma/products?categories%5B%5D=0&q=' + '+'.join(query)
    bousfiha_url="https://electrobousfiha.com/recherche?cat_id=all&controller=search&s="+"+".join(query)+"&spr_submit_search=Search&n=21&order=product.position.desc"
    marjmall_url="https://www.marjanemall.ma/catalogsearch/result/?q="+'+'.join(query)+"&product_list_order=most_viewed"
    ecplanet_url="https://www.electroplanet.ma/recherche?q="+'+'.join(query)
    avito_url="https://www.avito.ma/fr/maroc/"+'+'.join(query)+"--à_vendre"


    columns=scrape_jumia(jumia_url,base_jumia_url,query,choice)
    columns1=scrape_cosmos(cosmos_url,query)
    try:
        if bool(columns1['name']):
            columns['name'].append(columns1['name'][0])
            columns['price'].append(columns1['price'][0])
            columns['img url'].append(columns1['img url'][0])
    except:
        pass
    columns1 = scrape_bousfiha(bousfiha_url, query)
    try:
        if bool(columns1['name']):
            columns['name'].append(columns1['name'][0])
            columns['price'].append(columns1['price'][0])
            columns['img url'].append(columns1['img url'][0])
    except:
        pass
    columns1 = hard_scrap.scrape_marjane(marjmall_url, query)
    try:
        if bool(columns1['name']):
            columns['name'].append(columns1['name'][0])
            columns['price'].append(columns1['price'][0])
            columns['img url'].append(columns1['img url'][0])
    except:
        pass
    columns1 = hard_scrap.scrape_avito(avito_url, query)
    try:
        if bool(columns1['name']):
            columns['name'].append(columns1['name'][0])
            columns['price'].append(columns1['price'][0])
            columns['img url'].append(columns1['img url'][0])
    except:
        pass
    columns1 = hard_scrap.scrape_electroplanet(ecplanet_url, query)
    try:
        if bool(columns1['name']):
            columns['name'].append(columns1['name'][0])
            columns['price'].append(columns1['price'][0])
            columns['img url'].append(columns1['img url'][0])
        return columns
    except:
        return columns
if __name__ == '__main__':
    query = input("item name: ").lower().split()
    choice = input("1- Telephone \n2-Accessoires \n3-Smart watch \n4-Televisions et video\n5-Ordinateurs \nchoice:")
    products= scrape_products(query,choice)
    for name, price, img_url in zip(products['name'], products['price'], products['img url']):
        print(name, price, img_url)
