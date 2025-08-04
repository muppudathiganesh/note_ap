from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('<int:pk>/edit/', views.note_update, name='note_update'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('', views.home_view, name='home'),

]
