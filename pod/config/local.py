import os
import dj_database_url
from .common import Common
from unipath import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = Path(__file__).ancestor(3)


class Local(Common):
    DEBUG = True

    SQL_LITE_DATABASE = os.getenv('SQL_LITE_DATABASE', False)

    if SQL_LITE_DATABASE:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.config(
                default='postgres://postgres:@postgres:5432/postgres',
                conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
            )
        }

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=pod'
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
