from django.urls import path
from crudapp.views import *
from . import views

urlpatterns = [
    path('', emp),
    path('show', show),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete)

]
