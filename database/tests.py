import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')
django.setup()

from django.test import TestCase
from .device_forms import DevicesForm

# Create your tests here.

form = DevicesForm()
print(form)