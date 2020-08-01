from django.contrib import admin
from django.urls import path, include
import Wookie.views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Wookie.views.main, name="main"),
    path('Wookie/', include('Wookie.urls')),
]
