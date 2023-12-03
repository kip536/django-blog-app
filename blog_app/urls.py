from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',login_required(views.HomeView.as_view()), name="home"),
    path('article/<int:pk>', login_required(views.ArticleDetailView.as_view()), name="article-detail"),
    path('createPost/', login_required(views.CreatePostView.as_view()), name="createPost"),
    path('article/edit/<int:pk>', login_required(views.UpdatePostView.as_view()), name="update_post"),
    path('article/<int:pk>/delete', login_required(views.DeletePostView.as_view()), name="delete_post"),
    path('article/<int:pk>/comment/', login_required(views.CreateCommentView.as_view()), name="createcomment"),
    path('search_blog/', views.SearchBlog, name="search_blog"),
    path('profile/<int:pk>', login_required(views.UserDetailView.as_view()), name="profile"),
    
    
    #path('dashboard/',views.HomeView.as_view(),name="dashboard"),
    #path('login/',LoginView.as_view(),name="login_url"),
    #path('register/',views.registerView,name="register_url"),
    #path('logout/',LogoutView.as_view(next_page="dashboard"),name="logout"),
]