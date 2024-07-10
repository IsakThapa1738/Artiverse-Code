
from django.urls import path
from . import views
from Artists import views as views_artist

urlpatterns = [
    path('create/', views.artwork_create, name='artwork_create'),
    path('update/<int:id>/', views.artwork_update, name='artwork_update'),
    path('delete/<int:id>/', views.artwork_delete, name='artwork_delete'),
    path('artist_artwork/',views_artist.artist_artwork, name='artist_artwork'),
    path('art_details/<int:id>/', views.art_details, name='art_details'),

]