from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from requests_html import HTMLSession
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
with open('stock.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    driver.get("https://economictimes.indiatimes.com/markets/stocks/news")
    la=[]
    ##for _ in range(10):
    ##    driver.execute_script("window.scrollBy(0,800)")
    ##    time.sleep(6)
    ####session=HTMLSession()
    ####resp=session.get("https://economictimes.indiatimes.com/markets/stocks/news")
    html= driver.execute_script("return document.documentElement.outerHTML")
    soup=BeautifulSoup(html,'html.parser')
    h=soup.find_all('div','_class'=="eachStory")
    for ele in h:
        ell=ele.find('a',{ 'data-orefid':True})
        try:
            la.append(ell.text)
        except:
            continue
    writer.writerow(la)
    for i in range(15,0,-1):
        lb=[]
        driver.get("https://www.moneycontrol.com/news/business/stocks/page-"+str(i))
        html= driver.execute_script("return document.documentElement.outerHTML")
        soup=BeautifulSoup(html,'html.parser')
        h=soup.find_all('li','_class'=='clearfix')
        for ele in h:
            try:
                lb.append(((ele.find('h2')).find('a')).text)
            except:
                continue
        writer.writerow(lb)    

driver.quit()        
##print(soup.prettify())
##h=resp.html.xpath('//div[@class="eachStory"]/h3/a[1]')
##print(h.text)
##for ele in h:
##    print(ele.text)
##
##
##print(resp.html.xpath('//div[@class="autoload_continue"]',first=True).text)    
