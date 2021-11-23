from django.urls import path
from . import views

urlpatterns = [
    path("sample/",views.show,name='show'),
    path("add/",views.add,name='add'),
]
