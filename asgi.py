import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_profile_identification.settings')

application = get_asgi_application()
