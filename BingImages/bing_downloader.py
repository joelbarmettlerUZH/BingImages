import bs4
import requests
import re
import os

class BingImages():
    def __init__(self, topic, count=35, size=None, color=None, type=None, layout=None, person=None, age=None, licensetype=None):
        self.__topic = topic.replace(" ","+")
        self.__count = count
        self.__baseUrl = self.__assembleLink(size, color, type, layout, person, age, licensetype)
        self.__urls = set([])

    def __assembleLink(self, size, color, type, layout, person, age, licensetype):
        filters = ""

        possibleSizes = ["small", "medium", "large", "wallpaper"]
        possibleColors = ["yellow", "orange", "green", "red", "teal", "black", "white", "grey", "blue", "purple", "pink", "brown", "gray"]
        possibleTypes = ["photo", "clipart", "linedrawing", "animatedgif", "transparent"]
        possibleLayouts = ["square", "wide", "tall"]
        possiblePersons = ["face", "portrait"]

        ageDict = {
            "day":"lt1440",
            "week":"lt10080",
            "month":"lt43200",
            "year":"lt525600"
        }

        licenseDict = {
            "creativeCommons":"Type-Any",
            "publicDomain":"-L1",
        }

        if size in possibleSizes:
            filters += "+filterui:imagesize-"+size.upper()
        if color in possibleColors:
            filters += "+filterui:color2-FGcls_"+color.upper()
        if type in possibleTypes:
            filters += "+filterui:photo-"+type.lower()
        if layout in possibleLayouts:
            filters += "+filterui:aspect-"+layout.lower()
        if person in possiblePersons:
            filters += "+filterui:face-"+person.lower()
        if age in ageDict.keys():
            filters += "+filterui:age-"+ageDict[age]
        if licensetype in licenseDict.keys():
            filters += "+filterui:license"+licenseDict[licensetype]

        url = "https://www.bing.com/images/async?q=" + self.__topic +"&first=0&count=" + str(self.__count) + "&relp=" + str(self.__count) + "&qft=" + filters + "&lostate=c&mmasync=1&dgState=c*5_y*1640s1812s1758s1694s1705_i*36_w*186&IG=EABACC36F4F145FE94A4536B89DE0E49&SFX=2&iid=images.5662"
        return url

    def get(self):
        html = requests.get(self.__baseUrl).content
        soup = bs4.BeautifulSoup(html, "lxml")
        urls = set([])

        for link in soup.findAll('a'):
            link = str(link)
            reg = re.findall('"murl":"(?s).*","turl":"', link)
            if len(reg) > 0:
                urls.add(reg[0][8:-10])

        self.__urls = urls
        return urls

    @staticmethod
    def download(urls, folder="."):
        if not os.path.exists(folder):
            os.makedirs(folder)
        for link in urls:
            try:
                link = link.replace("\\","/")
                imgName = link[len(link) - 1 - link[::-1].index("/"):]
                if "?" in imgName:
                    imgName = imgName[:len(imgName) - 1 - imgName[::-1].index("?")]
                r = requests.get(link, stream=True)
                with open(folder + "/" + imgName, 'wb') as f:
                    for chunk in r.iter_content():
                        f.write(chunk)
            except Exception:
                pass

if __name__ == "__main__":
    musk = BingImages("Vitalik buterin", count=5).get()
    print(musk)