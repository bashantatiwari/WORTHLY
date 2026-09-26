import os
from pathlib import Path
from urllib.parse import urlparse, unquote

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-only-change-me-before-production')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']
if os.environ.get('VERCEL_URL'):
    ALLOWED_HOSTS.append(os.environ['VERCEL_URL'])
CSRF_TRUSTED_ORIGINS = ['https://*.vercel.app']

INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','vision','accounts']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'backend.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'backend.wsgi.application'

def database_config():
    url = os.environ.get('DATABASE_URL')
    if not url:
        return {'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}
    parsed = urlparse(url)
    return {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':unquote(parsed.path.lstrip('/')),
        'USER':unquote(parsed.username or ''),
        'PASSWORD':unquote(parsed.password or ''),
        'HOST':parsed.hostname or '',
        'PORT':parsed.port or 5432,
        'CONN_MAX_AGE':60,
        'OPTIONS':{'sslmode':'require'} if parsed.hostname not in ('localhost','127.0.0.1') else {},
    }
DATABASES = {'default': database_config()}
AUTH_PASSWORD_VALIDATORS = [
 {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
 {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
 {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
 {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE='en-us'; TIME_ZONE='UTC'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATIC_ROOT=BASE_DIR/'staticfiles'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='login'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
