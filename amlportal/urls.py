from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# الصفحة الرئيسية للموقع (home.html)
def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    # 🔸 لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 🔸 الصفحة الرئيسية (تفتح home.html)
    path('', home_view, name='home'),

    # 🔸 روابط التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),     # تسجيل الدخول / المستخدمين
    path('assessment/', include('assessment.urls')), # صفحات الأسئلة والسيناريوهات
    path('results/', include('results.urls')),       # نتائج التقييمات

    # ✅ لوحة القيادة (Dashboard)
    path('dashboard/', include('dashboard.urls')),
]

