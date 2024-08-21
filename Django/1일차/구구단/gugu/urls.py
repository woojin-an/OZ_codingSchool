"""
URL configuration for gugu project.

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
from django.shortcuts import render
from django.shortcuts import redirect

def gugu(request, num):
    if num < 2:
        return redirect('/gugu/2')

    context = {
        'num': num,
        'results': [num * i for i in range(1, 10)]
        # 'range': range(1, 10)
    }

    return render(request, template_name='gugu.html', context=context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gugu/<int:num>/', gugu),
]
