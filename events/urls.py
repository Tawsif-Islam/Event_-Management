from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('create/', views.event_create, name='event_create'),
    path('<int:event_id>/update/', views.event_update, name='event_update'),
    path('<int:event_id>/delete/', views.event_delete, name='event_delete'),

    
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/<int:participant_id>/update/', views.participant_update, name='participant_update'),
    path('participants/<int:participant_id>/delete/', views.participant_delete, name='participant_delete'),

  
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:category_id>/update/', views.category_update, name='category_update'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),

   
    path('dashboard/', views.dashboard, name='dashboard'),
]
