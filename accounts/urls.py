from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),

    path('logout/', views.logout_view, name='logout'),
]