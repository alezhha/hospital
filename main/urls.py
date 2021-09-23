from django.urls import path
from django.urls.resolvers import URLPattern
from .views import detail, index

urlpatterns = [
    path('', index, name = 'index'),
    path("detail/<int:pk>", detail, name="detail" )
]