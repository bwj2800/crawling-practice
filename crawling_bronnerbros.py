import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')

#3번 사이트
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
webpage=requests.get('https://bronnerbros.com/exhibitor-list/', headers=headers)

soup=BeautifulSoup(webpage.content, "html.parser")
frame = soup.find('iframe', attrs={"class":"iframe-class"})

res1 = requests.get(frame['src'])
frame_soup = BeautifulSoup(res1.content, 'html.parser')
frame2 = frame_soup.find('frame')

res2 = requests.get(frame2['src'])
frame_soup2 = BeautifulSoup(res2.content, 'html.parser')

# # BeautifulSoup으로 기업명 저장
# exhibitor_list = frame_soup2.find_all('a', attrs={"class":"ex"})
f = open("bronnerbros.txt", 'w', encoding='utf-8')
# for item in exhibitor_list:
#     f.write(item.text.strip()+"\n")

# selenuim으로 기업명 저장 및 기업명 클릭 후 상세 설명 저장
driver.get(frame2['src'])
sample = driver.find_elements(By.CLASS_NAME, "ex")
for item in sample:
    f.write(item.text.strip()+"|") # 기업명 저장
    item.send_keys('\n') # 클릭
    time.sleep(2)
    desc = driver.find_element(By.XPATH, '//*[@id="profileTab"]/div')
    f.write(desc.text.replace("\n"," ")+"\n") # 기업 상세 설명 저장

f.close()

