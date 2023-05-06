import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(host=os.environ.get('DB_HOST'),
                        user=os.environ.get('DB_USER'),
                        password=os.environ.get('DB_PASSWORD'),
                        db=os.environ.get('DB_NAME'),
                        charset='utf8')

cur = conn.cursor()

#table 생성
cur.execute("create table company( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(60) NOT NULL, address VARCHAR(100), type VARCHAR(50), owner VARCHAR(50), contact VARCHAR(30), website VARCHAR(50), item VARCHAR(50), description VARCHAR(4000), PRIMARY KEY(id));")

# medisvc 데이터 저장
f1 = open("medisvc.txt", 'r', encoding='utf-8')
lines = f1.readlines()   
for line in lines:   
    data=line.split('|')
    name=data[0].strip()
    address=data[1].strip()
    type=data[2].strip()
    owner=data[3].strip()
    cur.execute("INSERT INTO company (name, address, type, owner) VALUES(%s, %s, %s, %s)", (name, address, type, owner))

f1.close()


# bronnerbros 데이터 저장
f2 = open("bronnerbros.txt", 'r', encoding='utf-8')
lines = f2.readlines()   
for line in lines:   
    data=line.split('|')
    name=data[0].strip()
    description=data[1].strip()
    cur.execute("INSERT INTO company (name, description) VALUES(%s, %s)", (name, description))

f2.close()

conn.commit()
conn.close()