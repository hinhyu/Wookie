from django.contrib import admin
from django.urls import path
import Wookie.views

urlpatterns = [
    path('new/', Wookie.views.new, name='new'),
    path('create1', Wookie.views.create1, name='create1'),
    path('create2', Wookie.views.create2, name='create2'),
    path('create3', Wookie.views.create3, name='create3'),
    path('edit1/<int:pk>', Wookie.views.edit1, name='edit1'),
    path('edit2/<int:pk>', Wookie.views.edit2, name='edit2'),
    path('edit3/<int:pk>', Wookie.views.edit3, name='edit3'),
    path('delete/<int:pk>', Wookie.views.delete, name='delete'),
]
