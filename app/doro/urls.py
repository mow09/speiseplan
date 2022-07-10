from django.urls import path
from doro import views

app_name = 'doro'

urlpatterns = [
    # WARNING make sure you have them all in doro.views redefinded!!
    path('', views.IndexView.as_view(), name='index'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('details/', views.DetailsView.as_view(), name='details'),
    path('explore/', views.ExploreView.as_view(), name='explore'),
]
