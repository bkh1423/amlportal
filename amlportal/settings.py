from pathlib import Path

# 🔹 المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 مفتاح الأمان (احتفظي به سريًا)
SECRET_KEY = 'django-insecure-0v)g0h=(s@%p3o+#_zgxuh%=@$qtegfr7085zhilc68)=8eg#5'

# 🔹 وضع التطوير (خليه False لما ترفعين المشروع على الإنترنت)
DEBUG = True

ALLOWED_HOSTS = []


# =====================================================
# 🔹 التطبيقات (APPS)
# =====================================================

INSTALLED_APPS = [
    # Default Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'accounts',
    'assessment',
    'results',
]


# =====================================================
# 🔹 Middleware
# =====================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================================================
# 🔹 إعدادات المسارات والقوالب
# =====================================================

ROOT_URLCONF = 'amlportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مسار القوالب العامة (يمكن إنشاؤه لاحقًا)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'amlportal.wsgi.application'


# =====================================================
# 🔹 قاعدة البيانات (SQLite الافتراضية)
# =====================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================================================
# 🔹 التحقق من كلمات المرور
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =====================================================
# 🔹 اللغة والمنطقة الزمنية
# =====================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =====================================================
# 🔹 الملفات الثابتة (Static files)
# =====================================================

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# =====================================================
# 🔹 الإعدادات الافتراضية لمعرف الحقول
# =====================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
