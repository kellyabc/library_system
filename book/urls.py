from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
    path('index/', views.book_list, name="index"),
    path('<int:pk>/del_book/', views.del_book, name="del_book"),
    path('<int:pk>/edit_book/', views.edit_book, name="edit_book"),
    path('add_book/', views.add_book, name="add_book"),
]
