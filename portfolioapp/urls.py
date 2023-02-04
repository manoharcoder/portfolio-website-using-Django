from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('home',views.Home,name='Home'),
    path('about',views.About,name='About'),
    path('contact',views.handleContact,name='handleContact'),
    path('blog',views.handleBlog,name='handleBlog'),
    path('services',views.Services,name='Services'),
    path('resume',views.Resume,name='Resume'),
    path('internshipdetails',views.internshipDetails,name='internshipDetails'),
   

]