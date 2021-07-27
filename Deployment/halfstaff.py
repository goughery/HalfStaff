from bs4 import BeautifulSoup
import urllib.request
import re
from datetime import datetime

def scrape():
    page = urllib.request.urlopen("http://us.halfstaff.org")
    soup = BeautifulSoup(page, "html.parser")
    #print(soup.prettify())
    dates = soup.find_all('div', class_="date")
    
    startdate = dates[0]
    enddate = dates[1]
    
    desc = str(soup.find('div', class_="short"))
    desc = re.split("[<>]", desc)[2]
    uid = datetime.utcnow().isoformat()
    uid = uid.replace(".","").replace(":","").replace("-","")
    
    startdate = str(startdate).split("<strong>")[1].split("</strong>")[0].split("/")
    enddate = str(enddate).split("<strong>")[1].split("</strong>")[0].split("/")

    month = startdate[0]
    day = startdate[1]
    year = startdate[2]
    if len(month) == 2:
        month = month
    else:
        month = "0" + month
    if len(day) == 2:
        day = day
    else:
        day = "0" + day
    startdate = month + "-" + day + "-" + year

    uid = datetime.utcnow().isoformat()
    uid = uid.replace(".","").replace(":","").replace("-","")

    month = enddate[0]
    day = enddate[1]
    year = enddate[2]
    if len(month) == 2:
        month = month
    else:
        month = "0" + month
    if len(day) == 2:
        day = day
    else:
        day = "0" + day
    enddate = month + "-" + day + "-" + year
    

    #print(startdate, enddate)

    startdate_dt = datetime.strptime(startdate, '%m-%d-%Y')
    enddate_dt = datetime.strptime(enddate, '%m-%d-%Y')

    if startdate_dt >= datetime.now() and enddate_dt >= datetime.now():
        desc = desc
        yn = 1
    else:
        yn = 0
        desc = "The United States flag flies at full mast today."
    
    
    return startdate, enddate, desc, uid, yn

startdate, enddate, desc, uid, yn = scrape()

print(scrape())
