from django.urls import path
from todoapp.views import index,update_todo,create_todo,list_all_todos,delete_todo,Create_Book,list_all_books,B_Delete

urlpatterns = [
    path('',index,name="home"),
    path('create',create_todo,name="create"),
    path('list',list_all_todos,name="list"),
    path('delete/<int:id>',delete_todo,name="delete"),
    path('createBook',Create_Book,name="boook"),
    path('Listbook',list_all_books,name='listbooks'),
    path('del/<int:id>',B_Delete,name='Bdel'),
    path('update/<int:id>',update_todo,name='update')
]