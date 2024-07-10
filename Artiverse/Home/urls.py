from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="index"),
    path('explore/',views.explore, name="explore"),
    path('query/',views.search, name="query"),
    
]