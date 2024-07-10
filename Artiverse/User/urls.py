from django.urls import path
from . import views
urlpatterns=[
    path('create_user/',views.create_user, name='create_user'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('address/',views.billing_address, name='billing_address'),
    # path('wishlist/<int:id>/toggle/', views.toggle_wishlist, name='toggle_wishlist'),
]