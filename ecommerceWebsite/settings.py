from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Import Django environ and initialise environment variables
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INTERNAL_IPS = env.list('INTERNAL_IPS')

CSRF_TRUSTED_ORIGINS = ['https://ecommercewebsite-zcj7.onrender.com']


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

AUTH_USER_MODEL = 'account.CustomUser'

LOGIN_URL = '/login-view'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_tailwind',

    'paypal.standard.ipn',

    'django_filters',

    'account',
    'admin_panel',
    'cart',
    'chat',
    'client',   
    'core',
    'orders',
    'payments',
    'shop.apps.ShopConfig',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerceWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_total_items',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerceWebsite.wsgi.application'
ASGI_APPLICATION = 'ecommerceWebsite.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if not DEBUG:
    # PostgreSQL database (production)
    import dj_database_url
    
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL')
        )
    }

else:    
    # SQlite database (development - default)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Amazon S3 Configuration (for production)
if DEBUG:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
    }

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    AWS_S3_FILE_OVERWRITE = False
    
else:
    # Local static and media files configuration (for development)
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [BASE_DIR / 'static']
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email Configuration

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# Paypal

PAYPAL_RECEIVER_EMAIL = env('PAYPAL_RECEIVER_EMAIL')
PAYPAL_TEST = env.bool('PAYPAL_TEST')  
PAYPAL_BUY_BUTTON_IMAGE = env('PAYPAL_BUY_BUTTON_IMAGE')