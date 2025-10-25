from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# الصفحة الرئيسية للموقع
def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # تطبيقات المشروع
    path('accounts/', include('accounts.urls')),
    path('assessment/', include('assessment.urls')),
    path('results/', include('results.urls')),

    # ✅ أضيفي هذا السطر لربط الداشبورد
    path('dashboard/', include('dashboard.urls')),
]
