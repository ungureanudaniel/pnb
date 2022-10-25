from django.urls import path, include
from django.conf import settings
import debug_toolbar
from .views import home, gallery, snippet_detail
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    #-------sitemap snippet link-----------
    path('<slug:slug>', snippet_detail),
    #------ general urls-------------------
    path('', home, name="home"),
    path('gallery', gallery, name="gallery"),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
