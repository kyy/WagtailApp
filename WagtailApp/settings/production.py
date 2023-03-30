from .base import *

""" dont forget to delete auto-reload browser scripts in 'WagtailApp/templates/base.html' template """

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r%ih51zmqqm!s&--=r3b--(cpi$c%0^%2a_gg3!mihr#_&sy)$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# correct collecting staticfiles
MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# define the correct URLs:
STATIC_URL = "WagtailApp/static/"
MEDIA_URL = "WagtailApp/media/"
STATIC_ROOT = '/home/UNIX_USER/public_html/WagtailApp/static/'
MEDIA_ROOT = '/home/UNIX_USER/public_html/WagtailApp/media/'


try:
    from .local import *
except ImportError:
    pass
