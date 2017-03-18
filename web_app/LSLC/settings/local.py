from .__init__ import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'STORAGE_ENGINE': 'InnoDB',
        'NAME': 'lslcdb',
        'USER': 'root',
        'PASSWORD': 'a',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
        }
    }
}