from django.urls import path
from .views import Home, about, contact, products, singleProduct, add_cart, view_cart, remove_item, update

app_name = 'mainsite'
urlpatterns = [
    path('', Home, name='Home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('products', products, name='products'),
    path('single-product/<int:id>', singleProduct, name='single-product'),
    path('add-cart/<int:id>', add_cart, name='add-cart'),
    path('view-cart', view_cart, name='view-cart'),
    path('remove-item/<int:id>', remove_item, name='remove-item'),
    path('update/<int:id>', update, name='update'),
 ]