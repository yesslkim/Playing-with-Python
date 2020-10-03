import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EA%B9%80%ED%83%9C%EB%A6%AC") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

images2 = soup.select('#imgList > div > a > img')
num=1

for image in images2:
    img = image['src']
    dload.save(img,f'images2/{num}.jpg')
    num+=1

driver.quit() # 끝나면 닫아주기