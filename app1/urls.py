
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('about', views.about,name = 'about'),
    path('service',views.service,name='service'),
    path('project',views.project,name='project'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('send-form-email/',views.SendFormEmail.as_view(),name='send_email'),

    ]
