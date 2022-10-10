import requests
from bs4 import BeautifulSoup
"""
This module scraps meteoblue.com and is fetching temperature data and atmosphere
pictogram with a short description
"""
class WeatherApp:
    def __init__(self, url: str, findall1_tag: str, findall1_attr: str, findall1_attr_name: str, findall2_tag: str, findall2_attr: str, findall2_attr_name: str):
        self.url = url
        self.result = []
        self.findall1_tag = findall1_tag
        self.findall1_attr = findall1_attr
        self.findall1_attr_name = findall1_attr_name
        self.findall2_tag = findall2_tag
        self.findall2_attr = findall2_attr
        self.findall2_attr_name = findall2_attr_name
    def fetch_data():
        """
        get data from the specific website url using requests.get and
        beautifulsoup4
        """
        try:
            file = requests.get(self.url)
            self.soup = BeautifulSoup(file.content, "html.parser")
            return self.soup
        except Exception as e:
            print(e)

    def temp(self):
        """
        find all divs with attribute type and attribute name which holds the current
        temperature
        """
        try:
            temp = self.soup.find_all(self.findall1_tag, {self.findall1_attr:self.findall1_attr_name})[0].get_text().strip()[:2].strip()
            return temp
        except Exception as e:
            print(e)

        # print(content1[0].get_text().strip()[:2])
    def picto(self):
        """
        find all divs with attribute type and attribute name which holds the current
        weather description and picture
        """
        try:
            pic = self.soup.find_all(self.findall2_tag, {self.findall2_attr:self.findall2_attr_name})[0].find_all("img", src=True)[0]['src']
            return pic
        except Exception as e:
            print(e)
    def res(self):
        self.result.extend([temp(self.url, self.findall1_tag, self.findall1_attr, self.findall1_attr_name), picto(self.url, self.findall2_tag, self.findall2_attr, self.findall2_attr_name)])
        return self.result
    # img = content2[0].find_all("img", src=True)
    # list.extend([int(temp), pic])


if __name__ == "__main__":
    url1 = "https://www.meteoblue.com/en/weather/week/bucegi-mountains_romania_683598"
    url2 = "https://www.meteoblue.com/en/weather/week/everest-base-camp_china_10237388"
    tag1 = "div"
    tag2 = "span"
    attr1 = "class"
    attr2 = "class"
    attr_name1 = "h1 current-temp"
    attr_name2 = "current-picto"
    # results = list().extend([WeatherApp.temp(url1, tag1, attr1, attr_name1), WeatherApp.picto(url1, tag2, attr2, attr_name2)])
    WeatherApp(url1, tag1, attr1, attr_name1, tag2, attr2, attr_name2)
    # print(inst)












# for items in content:
#     for i in range(len(items.find_all("tr"))-1):
#         # create empty dictionary
#         dict = {}
#         try:
#             # assign value to given key
#             dict["day"]= items.find_all("span", {"class":"date-time"})[i].text
#             dict["date"]= items.find_all("span", {"class":"day-detail"})[i].text
#             dict["desc"]= items.find_all("td", {"class":"description"})[i].text
#             dict["temp"]= items.find_all("td", {"class":"temp"})[i].text
#             dict["precip"]= items.find_all("td", {"class":"precip"})[i].text
#             dict["wind"]= items.find_all("td", {"class":"wind"})[i].text
#             dict["humidity"]= items.find_all("td", {"class":"humidity"})[i].text
#         except:
#             # assign None values if no items are there with specified class
#             dict["day"]="None"
#             dict["date"]="None"
#             dict["desc"]="None"
#             dict["temp"]="None"
#             dict["precip"]="None"
#             dict["wind"]="None"
#             dict["humidity"]="None"
#         # append dictionary values to the list
#         list.append(dict)
