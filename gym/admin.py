from django.contrib import admin

from .models import Client
from .models import Pt
from .models import Session

admin.site.register(Client)
admin.site.register(Pt)
admin.site.register(Session)
