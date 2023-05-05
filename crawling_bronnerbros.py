import requests
from bs4 import BeautifulSoup 

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

exhibitor_list = frame_soup2.find_all('a', attrs={"class":"ex"})

f = open("bronnerbros.txt", 'w', encoding='utf-8')
for item in exhibitor_list:
    f.write(item.text.strip()+"\n")
f.close()