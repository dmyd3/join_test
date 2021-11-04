from django.contrib import admin
from q1.models import Cargo, Pessoa

# Register your models here.
admin.site.register(Cargo, admin.ModelAdmin)
admin.site.register(Pessoa, admin.ModelAdmin)