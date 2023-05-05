import requests
from bs4 import BeautifulSoup 

# 1번 사이트
webpage=requests.get('https://www.medisvc.com/cosmetics/fo/cosmeticscompanylist.sd')
# print(webpage)

soup=BeautifulSoup(webpage.content, "html.parser")
names=soup.find_all("a", attrs={'class':'text-theme-colored'})
names=soup.find_all("a", attrs={'class':'text-theme-colored'})
# ex_list=soup.find_all("ul", attrs={'class':'elementor-nav-menu'})

table = soup.find("table", attrs={"class":"table table-striped table-hover table-bordered"})
tbody = table.select_one('tbody')
trs = tbody.select('tr')

f = open("medisvc.txt", 'w', encoding='utf-8')

for tr in trs:
    name = tr.select('td')[0].text.strip()
    address = tr.select('td')[1].text.strip()
    type = tr.select('td')[2].text.strip()
    owner = tr.select('td')[3].text.strip()
 
    print('업체명: {0}, 주소: {1}, 업종: {2}, 대표자명: {3}'.format(name, address, type, owner))
    f.write(name+"|"+address+"|"+type+"|"+owner+"\n")
    
f.close()