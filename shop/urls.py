from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="About"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('hotproducts/', views.hotproducts, name="Hotproducts"),

]