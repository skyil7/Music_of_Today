from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('signupProc/',views.signupProc,name='signupProc'),
    path('loginProc/',views.loginProc,name='loginProc'),
    path('logout/',views.logout,name='logout'),
]