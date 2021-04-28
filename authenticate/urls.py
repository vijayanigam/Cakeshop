from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # path('done/', views.Logindone, name='done'),
]
