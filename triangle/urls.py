from django.urls import path

from triangle.views import triangle_calculate

app_name = 'triangle'
urlpatterns = [
    path('', triangle_calculate, name='index')
]
