from django.shortcuts import render, redirect
import requests
from .form import UserDataForm  # Import your UserDataForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_news(request):
    url = "https://inshortsapi.vercel.app/news?category=all"
    response = requests.get(url)
    data = response.json()
    return render(request, 'all_news.html', {'alldata': data})


def trending_news(request):
    url = "https://inshorts.me/news/topics/national?offset=0&limit=21"
    response = requests.get(url)
    data = response.json()
    return render(request, 'trending_news.html', {'trendingdata': data})


def top_news(request):
    url = "https://inshorts.me/news/top?offset=0&limit=21"
    response = requests.get(url)
    data = response.json()
    return render(request, 'top_news.html', {'topdata': data})


def entertainment_news(request):
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url)
    data = response.json()
    return render(request, 'entertainment_news.html', {'entertainmentdata': data})


def science_news(request):
    url = "https://inshortsapi.vercel.app/news?category=science"
    response = requests.get(url)
    data = response.json()
    return render(request, 'science_news.html', {'sciencedata': data})


def sports_news(request):
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url)
    data = response.json()
    return render(request, 'sports_news.html', {'sportsdata': data})


def sign_in(request):
    return render(request, 'sign_in.html')


def user_data_form(request):
    form = UserDataForm()

    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or any other page

    return render(request, 'register.html', {'form': form})
