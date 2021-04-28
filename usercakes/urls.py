from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('addtocart/<int:pk>/', views.AddToCart.as_view(), name='add_to_cart'),
    path('cart/', views.GetCart.as_view(), name='get_cart'),
    path('remove/', views.RemoveFromCart.as_view(), name='remove_from_cart'),
    path('placeorder/', views.PlaceOrder.as_view(), name='place_order'),
    path('myorders/', views.OrderRetrieveView.as_view(), name='create'),
]
