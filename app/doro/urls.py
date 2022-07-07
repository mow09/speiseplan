from django.urls import path
from doro import views

app_name = 'doro'

urlpatterns = [

    path('author/', views.AuthorView.as_view(), name='author'),


    path('create/', views.CreateView.as_view(), name='create'),


    path('details/', views.DetailsView.as_view(), name='details'),


    path('explore/', views.ExploreView.as_view(), name='explore'),


    path('index/', views.IndexView.as_view(), name='index'),

]
