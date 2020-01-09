from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('', views.index),
    path('login/', views.LoginView.as_view(), name='login'),
    #path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('register/', views.RegisterView.as_view(), name='register'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update', views.profile_update_view, name='profile_update'),
    path('profile/delete', views.profile_delete_view, name='profile_delete'),
    path('profile/password', views.password_edit_view, name='password_edit'),
]
