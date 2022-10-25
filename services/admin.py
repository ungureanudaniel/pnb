from django.contrib import admin
from .models import AttractionCategory, Attraction

class AttractionCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}

class AttractionAdmin(admin.ModelAdmin):
    fields = ['name', 'categ', 'slug']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Attraction, AttractionAdmin)
admin.site.register(AttractionCategory, AttractionCategoryAdmin)
