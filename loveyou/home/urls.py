from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name='index'),
    path('flames/',views.Flames,name='flames'),
    path('about/',views.about,name='about'),
    path('wishes',views.wishes,name='wishes')
]