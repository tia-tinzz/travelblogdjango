from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home,name='home'),
    path('login',v.loginpage,name='loginpage'),
    path('register',v.register,name='registerpage'),
    path('detail',v.detail,name='detail')
]
