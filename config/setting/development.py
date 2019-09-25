import os

from .base import *

# dev SECRET_KEY 노출되어도 무방, 실서버와는 다름
SECRET_KEY = ')j)0navo9wof1(va(qx-zzl7zquj6k+dmp)_p%cye8x)kp7-i+'
DEBUG = True

INSTALLED_APPS += [
   
]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3',),

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clip',  # clip
        'USER': 'root',  # root
        'PASSWORD': 'jeong337',
        'HOST': 'localhost',  # 공백으로 냅두면 default localhost
        'PORT': '3306'  # 공백으로 냅두면 default 3306
    }
}

MIDDLEWARE += [
   
]
