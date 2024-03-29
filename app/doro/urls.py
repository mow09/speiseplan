from django.urls import path
from doro import views

app_name = 'doro'

urlpatterns = [
    # WARNING make sure you have them all in doro.views redefinded!!
    path('', views.IndexView.as_view(), name='index'),
    path('ort/<slug:slug>/', views.PlaceView.as_view(), name='author'),
    # path('create/', views.CreateView.as_view(), name='create'),
    path('produkt/<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    # path('explore/', views.ExploreView.as_view(), name='explore'),
    path('produktpalette/', views.ProductsView.as_view(), name='products'),
    path('erfolg/', views.SuccessView.as_view(), name='contact_post'),
]
