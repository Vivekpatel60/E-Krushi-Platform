from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(form_class=CustomLoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add-data/', views.add_farmer_data, name='add_farmer_data'),
    path('edit-data/<int:pk>/', views.edit_farmer_data, name='edit_farmer_data'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve/<int:pk>/', views.approve_data, name='approve_data'),
    path('public-data/', views.public_data, name='public_data'),
]