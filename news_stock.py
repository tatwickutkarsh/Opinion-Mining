from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv
##options = Options()
##options.add_argument('--headless')
##options.add_argument('--disable-gpu')
##options.add_argument('--log-level=3')
driver=webdriver.Chrome(ChromeDriverManager().install())
##with open('stock.csv', mode='w',newline='') as file:
##    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
##    
##    driver.get("https://economictimes.indiatimes.com/markets/stocks/news")
##    
##    html= driver.execute_script("return document.documentElement.outerHTML")
##    soup=BeautifulSoup(html,'html.parser')
##    h=soup.find_all('div','_class'=="eachStory")
##    for ele in h:
##        la=[]
##        ell=ele.find('a',{ 'data-orefid':True})
##        try:
##            la.append(ell.text)
##            writer.writerow(la)
##        except:
##            continue
##    for i in range(15,0,-1):
##        
##        driver.get("https://www.moneycontrol.com/news/business/stocks/page-"+str(i))
##        html= driver.execute_script("return document.documentElement.outerHTML")
##        soup=BeautifulSoup(html,'html.parser')
##        h=soup.find_all('li','_class'=='clearfix')
##        for ele in h:
##            lb=[]
##            try:
##                lb.append(((ele.find('h2')).find('a')).text)
##                writer.writerow(lb)
##            except:
##                continue

##comp=[]        
##driver.get("https://www.bseindia.com/markets/equity/EQReports/mktwatchR.html?filter=gainer*all$all$")
##html= driver.execute_script("return document.documentElement.outerHTML")
##soup=BeautifulSoup(html,'html.parser')
##f=soup.find_all('tr',{'ng-repeat':"gl in GLData.Table.slice(((currentPage-1)*itemsPerPage), ((currentPage)*itemsPerPage)) track by gl.scrip_cd"})
##for ele in f:
##    x=ele.find('td')
##    print(x.text)
##    if int(x.text[0])>5:
##        h=ele.find('td',{'title':True})
##        print(h['title'])
##        comp.append(h['title'])
##    else:
##        comp.append(x.text)
##    h=ele.find('a',{'target':'_blank'})
##    try:
##        print(h.text)
##        comp.append(h.text)
##    except:
##        continue
##driver.get("https://www.bseindia.com/markets/equity/EQReports/mktwatchR.html?filter=loser*all$all$")
##html= driver.execute_script("return document.documentElement.outerHTML")
##soup=BeautifulSoup(html,'html.parser')
##f=soup.find_all('tr',{'ng-repeat':"gl in GLData.Table.slice(((currentPage-1)*itemsPerPage), ((currentPage)*itemsPerPage)) track by gl.scrip_cd"})
##for ele in f:
##    x=ele.find('td')
##    print(x.text)
##    if int(x.text[0])>5:
##        h=ele.find('td',{'title':True})
##        print(h['title'])
##        comp.append(h['title'])
##    else:
##        comp.append(x.text)      
##    h=ele.find('a',{'target':'_blank'})
##    try:
##        print(h.text)
##        comp.append(h.text)
##    except:
##        continue
with open('stock.csv', mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    comp=[]
    driver.get("https://www.moneycontrol.com/india/stockpricequote/")
    html= driver.execute_script("return document.documentElement.outerHTML")
    soup=BeautifulSoup(html,'html.parser')
    h=soup.find_all('tr',{'bgcolor':"#f6f6f6"})
    for ele in h:
        f=ele.find_all('td')
        for el in f:
    ##       print(el.a['href'])
    ##        print(el.a['href'].split('/'))
            a=el.a['href'].split('/')[6::]
            if len(a)==2:
                print(a)
                comp.append(a)
    
    print(len(comp))
    
    for ele in comp:
        link="http://www.moneycontrol.com/company-article/"+ele[0]+"/news/"+ele[1]
        for i in range(2):
            driver.get(link)
            html= driver.execute_script("return document.documentElement.outerHTML")
            soup=BeautifulSoup(html,'html.parser')
            try:
                h=soup.find_all('div',{'style':'width:550px'},class_='FL')
                for el in h:
                    print(el.a.strong.text)
                    writer.writerow([el.a.strong.text])
                f=soup.find('div',class_="pages MR10 MT15")
                if i==0:
                    print(f.a['href'])
                    link="https://www.moneycontrol.com"+f.a['href']
            except:
                continue
            
##print(comp)                  
driver.quit()        
