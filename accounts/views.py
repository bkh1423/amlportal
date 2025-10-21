from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile


# ========================
# 🔸 Register (Sign Up)
# ========================
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        company = request.POST.get('company_name', '').strip()
        role = request.POST.get('role', '').strip()

        # ✅ التحقق من المدخلات الأساسية
        if not username or not email or not password:
            messages.error(request, "Please fill in all required fields.")
            return redirect('register')

        # ✅ التحقق من تكرار المستخدم
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # ✅ إنشاء المستخدم الجديد
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, company_name=company, role=role)
            login(request, user)  # تسجيل الدخول مباشرة بعد الإنشاء
            messages.success(request, "Account created successfully! Welcome aboard.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')

    # إذا لم يكن الطلب POST
    return render(request, 'accounts/register.html')


# ========================
# 🔸 Login
# ========================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'accounts/login.html')


# ========================
# 🔸 Logout
# ========================
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home')


# ========================
# 🔸 Profile
# ========================
def profile_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to view your profile.")
        return redirect('login')

    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
        messages.error(request, "Profile not found.")

    return render(request, 'accounts/profile.html', {'profile': profile})
