from django.urls import path
from . import views

urlpatterns = [
    # path("", views.PostList.as_view(), name="home"),
    path("", views.RecipeList.as_view(), name="home"),
    path('add-recipe/', views.create_recipe, name='create_recipe'),
    path('edit-recipe/<slug:slug>', views.edit_recipe, name='edit_recipe'),
    path('delete-recipe/<slug:slug>', views.delete_recipe,
         name='delete_recipe'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
