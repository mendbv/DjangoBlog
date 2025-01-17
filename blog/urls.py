from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]