from django.urls import path
from . import views

urlpatterns = [

path('',views.Home,name='Home'),

path('login/',views.login_view,name='login'),
path('register/',views.registration,name='register'),
path('logout/',views.logout_view,name='logout'),

path('add-expense/',views.add_expense,name='add_expense'),
path('add-income/',views.add_income,name='add_income'),
path('delete-expense/<int:id>/',views.delete_expense,name='delete_expense'),
]