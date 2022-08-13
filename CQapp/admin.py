from django.contrib import admin
from CQapp.models import CqUser,CqTeam,Specialty

# Register your models here.
admin.site.register(CqUser)
admin.site.register(CqTeam)
admin.site.register(Specialty)
