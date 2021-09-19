from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Faculty)
admin.site.register(Position)
admin.site.register(Employee)

admin.site.register(Protocol)
admin.site.register(Theme)