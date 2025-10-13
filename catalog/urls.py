from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_video', views.create_film, name='create_film'),
    path('list', views.list_films, name='list_films'),
    path('edit/<int:pk>', views.update_film, name='update_film'),
    path('delete/<int:pk>', views.delete_film, name='delete_film'),
    path('report', views.lookup_film, name='lookup_film'),
]