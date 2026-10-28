from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
    path("category/<int:category_id>/delete/",views.delete_category,name="delete_category",),
    path("category/<int:category_id>/memo/<int:memo_id>/delete/",views.delete_memo,name="delete_memo",),
    path("category/<int:category_id>/memo/delete-selected/",views.delete_selected_memos,name="delete_selected_memos",),
    path("category/<int:category_id>/edit/",views.edit_category,name="edit_category",),
]
