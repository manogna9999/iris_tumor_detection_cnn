from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image_view, name='upload_image'),
    path('', views.home_view, name='home')
]
