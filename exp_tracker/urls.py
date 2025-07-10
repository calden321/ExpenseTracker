from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.ExpenseListView.as_view(), name='expenses'),  # Added trailing slash
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', 
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             redirect_authenticated_user=True
         ), 
         name='login'),
    path('accounts/logout/', 
         auth_views.LogoutView.as_view(next_page='home'), 
         name='logout'),
    # Include the auth URLs only once
    path('accounts/', include('django.contrib.auth.urls')),
]