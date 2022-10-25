from django.shortcuts import render
from utils.weatherapp import WeatherApp
from .forms import AttractionForm
from .models import Snippet

#==================snippet view for sitemaps===========================
def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'the detailview for slug of {slug}')

#========================home page=================================
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
    form = AttractionForm()
    return render(request, template, {"t":t})
#========================gallery page================================
def gallery(request):
    template = 'services/gallery_2.html'

    return render(request, template, {})
#========================? page================================
# def gallery(request):
#     template = 'services/gallery_2.html'
#
#     return render(request, template, {})
