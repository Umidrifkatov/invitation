from django.contrib import admin
from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'seating_place', 'unique_identifier',)
    search_fields = ('name', 'seating_place')  # Add fields for search
    list_filter = ('seating_place',)  # Add a filter for seating place

admin.site.register(Visitor, VisitorAdmin)



