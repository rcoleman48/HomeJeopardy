"""jeopardy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("single", views.single, name="single"),
    path("double", views.double, name="double"),
    path("<int:catnum>/<int:qnum>", views.question, name="question"),
    path("dailyd", views.dailyd, name="dailyd"),
    path("final", views.final, name="final"),
    path("double/<int:catnum>/<int:qnum>", views.question2, name="question2"),
    path("end", views.end, name="end")
]
