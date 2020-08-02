from django.contrib import admin
from django.urls import path, include
import Wookie.views
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Wookie.views.main, name='main'),
    path('new/', Wookie.views.new, name='new'),
    path('detail/<int:pk>/<int:user_id>', Wookie.views.detail, name='detail'),
    path('detail/<int:pk>/add/<int:user_id>', Wookie.views.add_comment, name="add_comment"),
    path('detail/<int:comment_id>/write/<int:user_id>', Wookie.views.write_message, name="write_message"),
    path('detail/<int:comment_id>/send/<int:user_id>', Wookie.views.send_message, name="send_message"),
    path('create', Wookie.views.create, name='create'),
    path('edit/<int:pk>', Wookie.views.edit, name='edit'),
    path('delete/<int:pk>', Wookie.views.delete, name='delete'),
    path('detail/<int:pk>/', Wookie.views.detail, name='detail'),
    path('beauty/<int:user_id>', Wookie.views.beauty, name='beauty'),
    path('art/<int:user_id>', Wookie.views.art, name='art'),
    path('other/<int:user_id>', Wookie.views.other, name='other'),
    path('accounts/', include('accounts.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
