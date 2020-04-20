from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_vlogs, name='all_vlogs'),
    path('<int:blog_id>/', views.detail, name='detail')

]

