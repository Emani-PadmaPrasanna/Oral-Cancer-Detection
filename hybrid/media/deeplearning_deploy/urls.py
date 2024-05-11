from django.contrib import admin
from django.urls import path
from deeplearning_deploy import views
urlpatterns=[
    path('',views.predict_image,name="predict_image"),
]