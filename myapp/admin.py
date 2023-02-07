from django.contrib import admin
from .models import TrainerModel

# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display=['empid','name','subject','salary']
    search_fields=['name','empid']

admin.site.register(TrainerModel,TrainerAdmin)