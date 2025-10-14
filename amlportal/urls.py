from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),

    path('accounts/', include('accounts.urls')),
    path('assessment/', include('assessment.urls')),
    path('results/', include('results.urls')),
]
