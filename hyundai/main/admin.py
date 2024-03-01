from django.contrib import admin
from .models import Vehicle
from ckeditor.widgets import CKEditorWidget
from django.db import models



class VehiclesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    
admin.site.register(Vehicle,VehiclesAdmin)