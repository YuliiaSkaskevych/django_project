from django.urls import path

from triangle.views import base, select, new_person, triangle_calculate, update

app_name = 'triangle'
urlpatterns = [
    path('', base, name="base"),
    path('triangle/', triangle_calculate, name='index'),
    path('person/', new_person, name="new_person"),
    path('person/<int:pk>/', update, name="update"),
    path('person/select/', select, name='select')
]
