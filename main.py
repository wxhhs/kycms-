import requests
import random


def go():
    years = 2022
    month = str(1).rjust(2,'0')
    day = str(4).rjust(2,'0')
    hours = 0
    min = 0
    ms = 0
    while years == 2022 :
        ms +=1
        if ms == 61:
            min +=1
            ms = 0
        if min == 60:
            hours +=1
            min = 0
        hourss = str(hours).rjust(2, '0')
        mins = str(min).rjust(2, '0')
        mss = str(ms).rjust(2, '0')
        url = "https://域名/public/database/"+str(years)+str(month)+str(day)+"-"+hourss+mins+mss+"-1.sql.gz"
        print(url)
        res = requests.get(url)
        print(res.status_code)
        if res.status_code == 200:
            print("ok")
            break

if __name__ == '__main__':
    go()

