"""
WSGI config for livingstructures project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livingstructures.settings')
os.environ["CLOUDINARY_CLOUD_NAME"] = "dhgzf5p5s"
os.environ["CLOUDINARY_API_KEY"] = "252759411793242"
os.environ["CLOUDINARY_API_SECRET"] = "HZhyko9fW5Bm8pzlU-n8Gdh-NGw"
application = get_wsgi_application()
