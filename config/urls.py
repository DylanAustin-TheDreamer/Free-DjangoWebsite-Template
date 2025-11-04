"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path #kept include if you set up a urls.py in an app later - I like this style

# Import the home view without app - simple view for home page that you can replace later
from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

# I'd advise setting up apps and their own urls.py and views.py right away for scalability, but for a simple template this is fine
#---------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]
