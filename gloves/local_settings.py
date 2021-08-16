from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
qwe
SECRET_KEY = 'wr5n5je4rv3js2dv3lj#3#!3!-ewf-r2e3v5je2r35w!-23wfl235w2j34#%23fv5p325kkp'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

