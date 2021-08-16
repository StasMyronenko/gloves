from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'wr5n5je4ergergassergeg!3!-ewf-r2e3v5je2r35w!-23wfl235w2j34#%23fv5p325kkp'


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gloves',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
