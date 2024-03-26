from django.contrib import admin 
from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('', views.index, name='home'), 
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        })),
]