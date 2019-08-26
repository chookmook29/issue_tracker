# Needed for Heroku deployment
import os

# Configuration for Heroku deployment, essential/otherwise won't deploy
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key as environmental variable for security
SECRET_KEY = "l18=*-$k-x!lu)x+^lt8k3cm=0j3mm+ugoqmi*e0l2h49bv)m%"

# Switched off in production
DEBUG = False

# Left empty because it doesn't affect Heroku deployment
ALLOWED_HOSTS = []


# App configuration feature used, needed if several apps in the same module
INSTALLED_APPS = [
    "ticket.apps.TicketsConfig",
    "blog.apps.BlogConfig",
    "checkout.apps.CheckoutConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "crispy_forms",
]
# No extra middleware added
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "issue_tracker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "issue_tracker.wsgi.application"


# Database details as environmental variables for security
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PSWD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
        "URI": os.environ.get("DATABASE_URL"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME":
     "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME":
     "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# User needed customization hence new model - Custom User
AUTH_USER_MODEL = "users.CustomUser"

# Changed to local language code to be more accurate
LANGUAGE_CODE = "en-gb"
# Changed to UK from US to prevent wrong timezone in comments timestamps
TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# AWS settings
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
    "CacheControl": "max-age=94608000",
}
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_REGION_NAME = "eu-west-2"
AWS_DEFAULT_ACL = None

# Base URL location from which static files will be served
STATIC_URL = "/static/"

# Additional directories that collectstatic tool should search for static files
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# MEDIA_ROOT used for development mode
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIAFILES_LOCATION = "media"
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# Improve form templates look
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Stripe details as environmental variables for security reasons
STRIPE_SECRET_KEY = os.environ.get("STRIPE_S")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_P")

# For Django-Heroku activation process, suppose to be at the bottom of the file
django_heroku.settings(locals())
