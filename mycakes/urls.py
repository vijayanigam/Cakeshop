from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('addcakes/', views.AddCakes.as_view(), name='addcakes'),
    path('cakes/<int:pk>/delete/', views.CakeDestroyView.as_view(), name='cake_delete'),
    path('showcake/<int:pk>/', views.CakeDetails.as_view(), name='cake_retrieve'),
    # path('searchcake/<str:pk>/', views.SearchDetails.as_view(), name='cake_search'),
    url(r'^searchcake/(?P<cakename>[a-zA-Z]+)$', views.SearchCakes.as_view(), name='cake_search'),
]
