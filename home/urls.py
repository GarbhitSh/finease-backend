from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
   
    path("testimonial",views.testimonial,name='testimonial'),
    path("team",views.team,name='team'),
    path("project",views.project,name='project'),
    path("feature",views.feature,name='feature'),
    path("contact",views.contact,name='contact'),
    #path("about",views.about,name='about'),



    


    path("signup",views.signup,name='signup'),
    path("login",views.LoginPage,name='login'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("marketing",views.marketing,name='marketing')


]
