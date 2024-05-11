from django.contrib import admin
from django.urls import path
from Oral_Predictor import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('home/', views.home,name='home'),
    path('predict/', views.predict, name='predict'),
    path('records/', views.db_record, name='records'),
    path('delete/<int:pk>', views.delete, name='delete')

]