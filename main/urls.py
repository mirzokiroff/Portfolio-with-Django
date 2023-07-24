from django.urls import path
from main.views import home, blog_single, portfolio_details, commentfunc

urlpatterns = [
    path('', home, name='index'),
    path('blog_single/', blog_single, name='blog_single'),
    path('portfolio_details/<int:id>', portfolio_details, name='portfolio_details'),
    path('post/<int:pk>/', commentfunc, name='post'),
]
