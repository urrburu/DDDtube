from django.contrib import admin
from .models import clip
# Register your models here.
class clipAdmin(admin.ModelAdmin):

    list_display = ['clipID','author','updated','id','title' ]
    raw_id_fields =['author']
    list_filter = ['updated','author']
    search_fields = ['text']
    ordering = ['-updated']

admin.site.register(clip, clipAdmin)
