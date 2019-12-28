import requests
from bs4 import BeautifulSoup
def getSoup(month, year):
    Dict = {
        "January":'01',
        "February":'02',
        "March":'03',
        "April":'04',
        "May":'05',
        "June":'06',
        "July":'07',
        "August":'08',
        "September":'09',
        "October":'10',
        "November":'11',
        "December":'12'
        }
    if month in Dict:
        a1 = 'http://explosm.net/comics/archive/'+str(year)+'/'+Dict[month.title()]
    else:
        a1=''
        print('enter month with first letter capitalised, check spelling, aborting')
        return False
    try:
        r = requests.get(a1)
        r.raise_for_status()
    except:
        print('wtf check intetrnet cant download %s'%(a1))
        return(a1)
    try:
        s = BeautifulSoup(r.text, 'html5lib')
    except:
        print(" bs not working, trying html parser, pip install html5lib")
        try:
            s = BeautifulSoup(r.text, 'html.parser')
        except:
            print(" bs still not working aborting")
            return False
            
    return s


