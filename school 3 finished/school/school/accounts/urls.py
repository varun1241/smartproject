from django.urls import path
from .views import register,login_process,logout_process,home,edit,passowrdchange,user,delete_user,add,show
from accounts import views
urlpatterns = [

path('',home),

path('register/',register,name="register"),
path('login/',login_process,name="login"),
path('logout/',logout_process,name="logout"),
path('delete/',delete_user,name="delete"),
path('home/',home,name="home"),
path('user/',user,name="user"),
path('edit/',edit,name="edit"),
path('changepassowrd/',passowrdchange,name="passwordchange"),

path('studentlist/', views.StudentList.as_view(), name='student-list'),
path('studentupadate/<pk>/',views.Studentupdate.as_view(),name='studentupadate'),
path("show/",show,name="show"),
path("add/",add,name="add"),
   
   

]
