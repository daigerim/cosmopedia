from django.urls import path
from .views import *

urlpatterns = [
    path('api/', CategoriesApiView.as_view(), name='categories_url'),
    path('api/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail_url'),
]