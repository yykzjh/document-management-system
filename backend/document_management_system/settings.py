"""
Django settings for document_management_system project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_BASE_DIR = os.path.join(BASE_DIR, "documents")
AVATAR_BASE_DIR = os.path.join(BASE_DIR, "User", "avatar")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)m8t+0434j+nj4-u8mb&%7bgr+&!!bsk&pg^n7yk_5a#$wdzk1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'User',
    'File',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'middleware.mymiddleware.AuthorizeToken',
]

ROOT_URLCONF = 'document_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'document_management_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dms',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'dms',
        'PASSWORD': 'dms'  
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TOKEN_EXPIRE = 60 * 60

BASE_LOG_DIR = str(BASE_DIR / 'log')

LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': str(Path(BASE_LOG_DIR) / 'xxx_info.log'),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': str(Path(BASE_LOG_DIR) / 'xxx_err.log'),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门定义一个收集特定信息的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': str(Path(BASE_LOG_DIR) / 'xxx_collect.log'),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
            'handlers': ['collect'],
            'level': 'INFO',
        }
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 配置白名单或者全部允许

# 全部允许配置
CORS_ORIGIN_ALLOW_ALL = True
# 允许cookie
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作

# # 允许的请求方式
# CORS_ALLOW_METHODS = (
#  'DELETE',
#  'GET',
#  'OPTIONS',
#  'PATCH',
#  'POST',
#  'PUT',
#  'VIEW',
# )
# # 允许的请求头
# CORS_ALLOW_HEADERS = (
#  'XMLHttpRequest',
#  'X_FILENAME',
#  'accept-encoding',
#  'authorization',
#  'content-type',
#  'dnt',
#  'origin',
#  'user-agent',
#  'x-csrftoken',
#  'x-requested-with',
#  'Pragma',
# )


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False   #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'   #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 465     #发件箱的SMTP服务器端口
# EMAIL_PORT = 25     # TLS传输协议使用25号端口
EMAIL_HOST_USER = 'yykzhjh@163.com'    #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'XHQLVCLKZPHTINNW'         #发送邮件的邮箱密码(这里使用的是授权码)
DEFAULT_FROM_EMAIL = 'Jiahui Zhong<yykzhjh@163.com>'