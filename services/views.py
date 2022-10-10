from django.shortcuts import render
from utils.weatherapp import WeatherApp
def home(request):
    template = 'services/index3.html'
    url1 = "https://www.meteoblue.com/en/weather/week/bucegi-mountains_romania_683598"
    tag1 = "div"
    attr1 = "class"
    attr_name1 = "h1 current-temp"
    tag2 = "span"
    attr2 = "class"
    attr_name2 = "current-picto"
    t = WeatherApp(url1, tag1, attr1, attr_name1, tag2, attr2, attr_name2)
    return render(request, template, {"t":t})
