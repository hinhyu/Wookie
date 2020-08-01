from django.contrib import admin
from django.urls import path
import Wookie.views

urlpatterns = [
    path('new/', Wookie.views.new, name='new'),
    path('detail/<int:pk>/add', Wookie.views.add_comment, name="add_comment"),
    path('delete/<int:pk>', Wookie.views.delete, name='delete'),
    path('detail/<int:pk>/', Wookie.views.detail, name='detail'),
    path('beauty/', Wookie.views.beauty, name='beauty'),
    path('art/', Wookie.views.art, name='art'),
    path('other/', Wookie.views.other, name='other'),
]