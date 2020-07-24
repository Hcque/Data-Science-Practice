from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.
admin.site.register(Event)
admin.site.register(Guest)
"""
python manage.py shell

Event.object.create(id=3, name='红米MAX发布会', limit=2000, status=True,address='北京会展中心',start_time=datetime(2016,9,22,14,0,0))
"""

