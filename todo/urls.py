from django.urls import path
from . import view_index,view_create,view_update,view_delete
urlpatterns=[
    path('',view_index.index,name='selectAll'),
    path('list/',view_index.index,name='selectAll'),
    path('add/',view_create.create,name = 'add'),
    path('delete/<int:id>/',view_delete.delete),
    path('edit/',view_update.update)
]