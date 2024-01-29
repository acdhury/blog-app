from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blogs/', views.blogs, name="blogs"), 
    path("add-blog/",views.add_blog, name = "add-blog"), 
    path('blogs/<int:blog_id>/delete/', views.delete_blog, name='delete-blog'),
    path('blogs/<int:id>/update/', views.update_blog, name="update-blog")
]


