import requests
from bs4 import BeautifulSoup
import random

colors=["\033[0;30m","\033[0;31m","\033[0;32m","\033[0;33m","\033[0;34m","\033[0;35m","\033[0;36m","\033[0;37m","\033[1;30m","\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"]
print(random.choice(colors)+"\n% % % % % % % % % % % % % % % % % % % % % % % % % %\n"+random.choice(colors)+" "*52+"%\n"+random.choice(colors)+"╔═══╦═══╦═══╦═══╦╗──╔═══╗"+random.choice(colors)+"╔╗──╔══╦═╗─╔╦╗╔═╗          %\n"+random.choice(colors)+"║╔═╗║╔═╗║╔═╗║╔═╗║║──║╔══╝"+random.choice(colors)+"║║──╚╣╠╣║╚╗║║║║╔╝          %\n"+random.choice(colors)+"║║─╚╣║─║║║─║║║─╚╣║──║╚══╗"+random.choice(colors)+"║║───║║║╔╗╚╝║╚╝╝           %\n"+random.choice(colors)+"║║╔═╣║─║║║─║║║╔═╣║─╔╣╔══╝"+random.choice(colors)+"║║─╔╗║║║║╚╗║║╔╗║           %\n"+random.choice(colors)+"║╚╩═║╚═╝║╚═╝║╚╩═║╚═╝║╚══╗"+random.choice(colors)+"║╚═╝╠╣╠╣║─║║║║║╚╗          %\n"+random.choice(colors)+"╚═══╩═══╩═══╩═══╩═══╩═══╝"+random.choice(colors)+"╚╚═══╩══╩╝─╚═╩╝╚═╝         %\n"+random.choice(colors)+"\t\t\tGOOGLE LINK COLLECTOR       %\n"+random.choice(colors)+"\t\t\tCODED BY TMRSWRR            %\n"+random.choice(colors)+"\t\t\tHAPPY HACKING               %\n"+random.choice(colors)+" "*52+"%\n"+random.choice(colors)+"% % % % % % % % % % % % % % % % % % % % % % % % % %")

def search():
    try:
        search=input(random.choice(colors)+"Write search word :")
        page=input(random.choice(colors)+"Write page number :")
        word=input(random.choice(colors)+"example:anonfiles.com\nWhich website links :")
        count=0
        for i in range(int(page)):
            url=f"https://www.google.com/search?q=site:{word} {search}&client=firefox-b-d&ei=tI7EYLeWAoytrgScvoCYBA&start={count}&sa=N&ved=2ahUKEwi3wOrT85HxAhWMlosKHRwfAEMQ8NMDegQIARBU&biw=1368&bih=595"
            headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
            r=requests.get(url,headers=headers)
            s = BeautifulSoup(r.content, "lxml")
            c = s.findAll("div",{"class":"tF2Cxc"})[:10]
            links = [div.find('a') for div in c]
            hrefs = [link.get('href') for link in links]
            count+=10
            for i in hrefs:
                print(i)
        print(random.choice(colors)+"Finished search...")
    except:
        print(random.choice(colors)+"Missing or wrong value!!!")
search()
