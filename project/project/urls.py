from django.contrib import admin
from django.urls import include, path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('api.urls')),
]
