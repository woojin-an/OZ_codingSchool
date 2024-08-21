"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,Http404
from django.shortcuts import render

movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '웡카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},
]


def index(request):
    return HttpResponse("<h1>Hello</h1>")


def blog_list(request):
    # book_text = ''
    #
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'

    return render(request, template_name='../templates/book_list.html', context= {'range': range(0, 10)})


def book(request, num):

    return render(request, template_name='../templates/book_detail.html', context={'num': num})


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')


def python(request):
    return HttpResponse('python 페이지 입니다.')


def movies(request):
    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie["title"]}</a><br>'
    #     for index, movie in enumerate(movie_list)
    # ]
    #
    # response_text = '<br>'.join(movie_titles)
    #
    # return HttpResponse(response_text)
    return render(request, template_name='../templates/movies.html', context={'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]
    context = {'movie': movie, 'index': index}
    return render(request, template_name='../templates/movie.html', context=context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', blog_list),
    path('book_list/<int:num>/', book),

    path('language/<str:lang>/', language),
    path('language/python/', python),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
]
