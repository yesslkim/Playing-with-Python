# 이미지 웹 스크래핑(크롤링)하기
# 셀레니움 패키지 = 브라우저 제어용
# 뷰티풀숩 라이브러리 = 원하는거 가져오기
import dload

from bs4 import BeautifulSoup
from selenium import webdriver
import time # 파이썬 내장함수

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

# 이미지 한개 가져올 때 - 셀렉터로 가져오기
singleImage = soup.select_one('#imgList > div:nth-child(1) > a > img')['src']

# 이미지 여러개 가져올 때
images = soup.select('#imgList > div > a > img')

i=1
for image in images:
    img = image['src']
    dload.save(img,f'image/{i}.jpg')
    i+=1
    
driver.quit() # 끝나면 닫아주기
