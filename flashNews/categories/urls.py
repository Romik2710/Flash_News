from django.urls import path
from . import views
from .views import user_data_form

urlpatterns = [
    path('', views.index, name="indexfile"),
    path('all_news/', views.all_news, name="allnewsfile"),
    path('top_news/', views.top_news, name="topnewsfile"),
    path('trending_news/', views.trending_news, name="trendingnewsfile"),
    path('science_news/', views.science_news, name="sciencenewsfile"),
    path('entertainment_news/', views.entertainment_news, name="entertainmentnewsfile"),
    path('sports_news/', views.sports_news, name="sportsnewsfile"),
    path('sign_in/', views.sign_in, name="signinfile"),
    path('user_data_form/', views.user_data_form, name='user_data_form'),
]
