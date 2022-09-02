from django.contrib import admin
from django.urls import path
from .views import home , download_file , Commentview , Productsview

urlpatterns = [
    path('', home , name="home"),
    path('download/', download_file),
    path('comments/', Commentview.as_view()),
    path('products/', Productsview.as_view()),
]