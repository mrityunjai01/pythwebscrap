import requests
import os
from bs4 import BeautifulSoup
from f import getSoup

picdate = {}

def getPic(month, year, auth):
    global picdate
    picdate = {}
    picUrlList =[]
    s = getSoup(month, year)
    for tag in s.select('#comic-author'):
        if auth.title() in tag.contents[-1]:
            add = 'http:'+tag.parent.a.img['src']
            picUrlList.append(add)
            picdate[add]=tag.contents[0].strip()
    return picUrlList
    
def Download(fil, l, nem):
    for page in fil:
        p=os.path.join(os.getcwd(), l)
        if not os.path.isdir(p):
            os.makedirs(p)
        imageFile = open(os.path.join(p, nem+'.png'),'wb')
        for chunk in fil.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
def Final(month, year, author):
    for i in getPic(month, year, author):
        nem = picdate[i]
        nem += '-'+author
        Download(requests.get(i), os.path.join(str(year), month.lower()),nem)

