from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepagefunc, name='home'),
    path('post/<int:pk>/', views.blogfunc, name='post'),
    path('portfolio/<int:pk>/', views.portfoliofunc, name='portfolio'),
    path('register/', views.signupfunc, name='register'),
    path('login/', views.loginfunc, name='login'),
    path('my-profile/', views.my_profile_func, name='my-profile'),
    path('logout/', views.logoutfunc, name='logout'),
    path('update/', views.updatefunc, name='update'),
    path('add-skill/', views.add_skillfunc, name='add-skill'),
    path('add-service/', views.add_servicefunc, name='add-service'),
    path('add-blog/', views.add_blogfunc, name='add-blog'),
    path('add-portfolio/', views.add_portfoliofunc, name='add-portfolio'),
    path('add-statistic/', views.add_statistic, name='add-statistic'),
    path('update/skill/<int:pk>/', views.update_skillfunc, name='update-skill'),
    path('update/service/<int:pk>/', views.update_servicefunc, name='update-service'),
    path('update/blog/<int:pk>/', views.update_blogfunc, name='update-blog'),
    path('update/portfolio/<int:pk>/', views.update_portfoliofunc, name='update-portfolio'),
    path('delete/skill/<int:pk>/', views.delete_skillfunc, name='delete-skill'),
    path('delete/blog/<int:pk>/', views.delete_blogfunc, name='delete-blog'),
    path('delete/service/<int:pk>/', views.delete_servicefunc, name='delete-service'),
    path('delete/portfolio/<int:pk>/', views.delete_portfoliofunc, name='delete-portfolio'),
    path('partner-comment/<str:username>/', views.partner_commentfunc, name='partner-comment'),
    path('<str:username>/', views.userfunc, name='user')
]