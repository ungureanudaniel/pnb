from django.urls import path, include
from django.conf import settings
from .views import home
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    #------ general urls-------------------
    path('', home, name="home"),
    path('i18n/', include('django.conf.urls.i18n')),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
