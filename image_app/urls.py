from django.urls import path 
from . import views

app_name = "test_app"
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.test_view,name="test")
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)