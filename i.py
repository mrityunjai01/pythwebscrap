import os
from h import Final
yrs = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
mths = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

seq = []
for i in yrs:
    for j in mths:
        seq.append(i+" "+j)

def start():
    try:
        print('opening '+os.path.join(os.getcwd(), "input.txt"))
        f  = open('input.txt')
    except:
        print("cant open input.txt make sure that the file is named exactly inputDOTtxt\
              and is saved in the same folder")
        return False
    [date1, date2, author]=f.readlines()
    print('date1: %s date2: %s author: %s'%(date1.strip(),date2.strip(),author.strip()))
    date1=date1.strip()
    date2=date2.strip()
    author=author.strip().title()
    m1 = date1.split()[0].title()
    m2 = date2.split()[0].title()
    y1 = date1.split()[1]
    y2 = date2.split()[1]
    try:
        i1 = seq.index(y1+" "+m1)
        i2 = seq.index(y2+" "+m2)
        i = i1
    except:
        print("holy shit, the year should be from 2005 upto 2019, make sure that\
                spelling of month is right")
        return False
    
    if (i1>i2):
        print('start year/mnth should have been earlier than end year/mnth')
    while(i<=i2):
        s=seq[i].split()
        print("Working on %s %s"%(s[0],s[1]))
        Final(s[1],s[0],author)
        i+=1
        
    
