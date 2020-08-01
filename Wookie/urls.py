from django.contrib import admin
from django.urls import path, include
import Wookie.views
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Wookie.views.main, name='main'),
    path('new/', Wookie.views.new, name='new'),
    path('detail/<int:pk>/add', Wookie.views.add_comment, name="add_comment"),
    path('delete/<int:pk>', Wookie.views.delete, name='delete'),
    path('detail/<int:pk>/', Wookie.views.detail, name='detail'),
    path('beauty/', Wookie.views.beauty, name='beauty'),
    path('art/', Wookie.views.art, name='art'),
    path('other/', Wookie.views.other, name='other'),
    path('accounts/', include('accounts.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
