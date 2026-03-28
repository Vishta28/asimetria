from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('gallery_page/<slug:slug>/', views.gallery_page, name='gallery_page'),
    path('gallery_image_detail/<path:image_url>/<str:description>/', views.gallery_image_detail, name='gallery_image_detail')
]