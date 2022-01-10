from .base import *  # noqa

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': 'SET character_set_connection=utf8mb4;'
                            'SET collation_connection=utf8mb4_unicode_ci;'
                            "SET NAMES 'utf8mb4';"
                            "SET CHARACTER SET utf8mb4;"
        },
    },
    "Lunex1": {
        "ENGINE": "mssql",
        "NAME": env('DATABASE_NAME_LUNEX1'),
        "USER": env('DATABASE_USER_LUNEX1'),
        "PASSWORD": env('DATABASE_PASSWORD_LUNEX1'),
        "HOST": env('DATABASE_HOST_LUNEX1'),
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server"},
    },
}
