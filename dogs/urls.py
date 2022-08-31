from django.urls import path

from . import views

urlpatterns = [
  path('', views.index,  name='dogs'),
  path('<int:dog_id>', views.dog_detail,  name='dog_detail'),
  path('search', views.search, name='search')
]